import sqlite3
import time
import json
import requests
from typing import Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
from wbapi.easyheader import SecurityInterceptor, generate_device_id
import uuid
from urllib.parse import urlparse

class WBCourierAPI:
    def __init__(self, db_path: str = "wb_courier.db"):
        self.db_path = db_path
        self._init_database()
        
    def _init_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    phone TEXT PRIMARY KEY,
                    device_uuid TEXT,
                    device_name TEXT,
                    latitude REAL,
                    longitude REAL,
                    access_token TEXT,
                    refresh_token TEXT,
                    access_expires_at INTEGER,
                    refresh_expires_at INTEGER,
                    created_at INTEGER,
                    updated_at INTEGER
                )
            ''')
            conn.commit()
    
    def _get_user(self, phone: str) -> Optional[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE phone = ?', (phone,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def _update_user(self, phone: str, data: Dict):
        current_time = int(time.time())
        data['updated_at'] = current_time
        
        placeholders = ', '.join([f"{key}=?" for key in data.keys()])
        values = list(data.values()) + [phone]
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                UPDATE users SET {placeholders} WHERE phone = ?
            ''', values)
            conn.commit()
    
    def _create_user(self, phone: str, device_uuid: str, device_name: str, 
                    latitude: float, longitude: float):
        current_time = int(time.time())
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (
                    phone, device_uuid, device_name, latitude, longitude,
                    access_token, refresh_token, access_expires_at,
                    refresh_expires_at, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                phone, device_uuid, device_name, latitude, longitude,
                None, None, None, None, current_time, current_time
            ))
            conn.commit()
    
    def _get_headers(self, phone: str, url: str, is_auth: bool = False) -> Dict:
        """Получение заголовков для запроса"""
        user = self._get_user(phone)
        if not user:
            raise ValueError(f"Пользователь с телефоном {phone} не найден")
        
        # Парсим URL для получения хоста и пути
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        path = parsed_url.path
        if parsed_url.query:
            path += f"?{parsed_url.query}"
        
        # Создаем интерцептор с данными пользователя
        interceptor = SecurityInterceptor(
            zapp_version="4.91.2",
            zsignature_version="6f8f8ea7-0773-4cde-a70e",
            zdevice_id=user['device_uuid'],
            zdevice_name=user['device_name']
        )
        
        # Генерируем базовые заголовки
        headers = interceptor.generate_headers(
            website_host=host,  # Используем хост из URL
            path=path,          # Используем путь из URL
            latitude=user['latitude'],
            longitude=user['longitude'],
            #timestamp=1768821676
        )
        
        # Добавляем Accept header для всех запросов
        headers["Accept"] = "application/json, text/plain"
        
        # Для auth запросов добавляем Content-Type
        if is_auth:
            headers["Content-Type"] = "application/json; charset=UTF-8"
        
        # Для не-auth запросов добавляем Authorization
        if not is_auth:
            access_token = self._get_valid_access_token(phone)
            headers["Authorization"] = f"Bearer {access_token}"
            headers["Content-Type"] = "application/json; charset=UTF-8"
        
        return headers

    
    def _get_valid_access_token(self, phone: str) -> str:
        user = self._get_user(phone)
        if not user or not user['access_token']:
            raise ValueError("Пользователь не аутентифицирован")
        
        current_time = int(time.time())
        
        #expire..
        if current_time >= user['access_expires_at']:
            print("Access токен истек, обновляем...")
            self._refresh_token(phone)
            user = self._get_user(phone)
        
        return user['access_token']
    
    def _refresh_token(self, phone: str):
        user = self._get_user(phone)
        if not user or not user['refresh_token']:
            raise ValueError("Refresh токен не найден")
        
        current_time = int(time.time())
        
        if current_time >= user['refresh_expires_at']:
            raise ValueError("Refresh токен истек, требуется повторная аутентификация")
        
        url = "https://r-point.wb.ru/wbc/api/v1/courier/refresh"
        
        headers = self._get_headers(phone, url, is_auth=True)
        
        data = {
            "token": user['refresh_token']
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            
            current_time = int(time.time())
            access_expires = current_time + response_data['access']['ttl']
            refresh_expires = current_time + response_data['refresh']['ttl']
            
            self._update_user(phone, {
                'access_token': response_data['access']['token'],
                'refresh_token': response_data['refresh']['token'],
                'access_expires_at': access_expires,
                'refresh_expires_at': refresh_expires
            })
            print("Токены успешно обновлены")
        else:
            raise ValueError(f"Ошибка обновления токена: {response.status_code} - {response.text}")
    
    def auth(self, phone: str, device_uuid: Optional[str] = None, 
             device_name: Optional[str] = None, 
             latitude: float = 59.772022, longitude: float = 39.576505):
        existing_user = self._get_user(phone)
        
        if existing_user and existing_user['access_token']:
            current_time = int(time.time())
            if current_time < existing_user['access_expires_at']:
                print("Пользователь уже аутентифицирован")
                return
            elif current_time < existing_user['refresh_expires_at']:
                print("Access токен истек, обновляем...")
                self._refresh_token(phone)
                return
        
        if device_uuid is None:
            device_uuid = generate_device_id()
        
        if device_name is None:
            device_name = "huawei p30 pro"
        
        if existing_user:
            self._update_user(phone, {
                'device_uuid': device_uuid,
                'device_name': device_name,
                'latitude': latitude,
                'longitude': longitude,
                'access_token': None,
                'refresh_token': None,
                'access_expires_at': None,
                'refresh_expires_at': None
            })
        else:
            self._create_user(phone, device_uuid, device_name, latitude, longitude)
        
        url = "https://r-point.wb.ru/wbc/api/v1/login"
        headers = self._get_headers(phone, url, is_auth=True)
        
        data = {
            "device_type": "DEVICE_ANDROID",
            "device_uuid": device_uuid,
            "is_admin": False,
            "phone": phone
        }
        
        print(f"Отправляем запрос на отправку кода для телефона {phone}...")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            validation_token = response_data['data']
            code_length = response_data['code_length']
            
            print(f"Код отправлен. Длина кода: {code_length}")
            
            code = input(f"Введите {code_length}-значный код: ").strip()
            
            if len(code) != code_length:
                raise ValueError(f"Код должен содержать {code_length} цифр")
            
            url = "https://r-point.wb.ru/wbc/api/v1/courier/validate"
            headers = self._get_headers(phone, url, is_auth=True)
            
            data = {
                "code": code,
                "device_type": "DEVICE_ANDROID",
                "device_uuid": device_uuid,
                "token": validation_token
            }
            
            print("Проверяем код...")
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                response_data = response.json()
                
                current_time = int(time.time())
                access_expires = current_time + response_data['access']['ttl']
                refresh_expires = current_time + response_data['refresh']['ttl']
                
                self._update_user(phone, {
                    'access_token': response_data['access']['token'],
                    'refresh_token': response_data['refresh']['token'],
                    'access_expires_at': access_expires,
                    'refresh_expires_at': refresh_expires
                })
                
                print("Аутентификация успешна! Токены сохранены.")
                
            else:
                raise ValueError(f"Ошибка валидации: {response.status_code} - {response.text}")
                
        else:
            raise ValueError(f"Ошибка отправки кода: {response.status_code} - {response.text}")

    
    def request_with_query(self, phone: str, method: str, url: str, query_params: Dict = None):
        self._ensure_auth(phone)
        
        headers = self._get_headers(phone, url, is_auth=False)
        
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=query_params)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, params=query_params)
        else:
            raise ValueError(f"Неподдерживаемый метод: {method}")
        
        if response.status_code == 401:
            print("Получена 401 ошибка, пытаемся обновить токен...")
            self._refresh_token(phone)
            headers = self._get_headers(phone, url, is_auth=False)
            
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, params=query_params)
            else:
                response = requests.post(url, headers=headers, params=query_params)
        
        return response
    
    def request_with_body(self, phone: str, method: str, url: str, body: Dict = None):
        self._ensure_auth(phone)
        
        headers = self._get_headers(phone, url, is_auth=False)
        
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, json=body)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=body)
        else:
            raise ValueError(f"Неподдерживаемый метод: {method}")
        
        if response.status_code == 401:
            print("Получена 401 ошибка, пытаемся обновить токен...")
            self._refresh_token(phone)
            headers = self._get_headers(phone, url, is_auth=False)
            
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, json=body)
            else:
                response = requests.post(url, headers=headers, json=body)
        
        return response

    
    def update_coordinates(self, phone: str, latitude: float, longitude: float):
        self._update_user(phone, {
            'latitude': latitude,
            'longitude': longitude
        })
        print(f"Координаты обновлены: {latitude}:{longitude}")
    
    def get_info(self, phone: str) -> Dict:
        user = self._get_user(phone)
        if not user:
            return {"error": "Пользователь не найден"}
        
        current_time = int(time.time())
        
        info = {
            "phone": user['phone'],
            "device_uuid": user['device_uuid'],
            "device_name": user['device_name'],
            "latitude": user['latitude'],
            "longitude": user['longitude'],
            "access_token": user['access_token'],
            "refresh_token": user['refresh_token'],
            "access_expires_in": max(0, user['access_expires_at'] - current_time) if user['access_expires_at'] else None,
            "refresh_expires_in": max(0, user['refresh_expires_at'] - current_time) if user['refresh_expires_at'] else None,
            "is_authenticated": bool(user['access_token'] and user['access_expires_at'] and user['access_expires_at'] > current_time)
        }
        
        return info
    
    def logout(self, phone: str):
        user = self._get_user(phone)
        if not user or not user['access_token']:
            print("Пользователь не аутентифицирован")
            return
        
        current_time = int(time.time())
        if current_time >= user['access_expires_at']:
            print("Access токен уже истек")
            self._update_user(phone, {
                'access_token': None,
                'refresh_token': None,
                'access_expires_at': None,
                'refresh_expires_at': None
            })
            return
        
        url = "https://r-point.wb.ru/wbc/api/v1/logout"
        headers = self._get_headers(phone, url, is_auth=False)
        
        data = {
            "deviceType": "DEVICE_ANDROID"
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print("Выход выполнен успешно")
            else:
                print(f"Ошибка выхода: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Ошибка при отправке запроса выхода: {e}")
        
        self._update_user(phone, {
            'access_token': None,
            'refresh_token': None,
            'access_expires_at': None,
            'refresh_expires_at': None
        })
    
    def _ensure_auth(self, phone: str):
        user = self._get_user(phone)
        
        if not user:
            raise ValueError(f"Пользователь с телефоном {phone} не найден. Сначала выполните аутентификацию.")
        
        current_time = int(time.time())
        
        if not user['access_token'] or current_time >= user['access_expires_at']:
            if user['refresh_token'] and current_time < user['refresh_expires_at']:
                print("Access токен истек, обновляем...")
                self._refresh_token(phone)
            else:
                print("Токены истекли, требуется повторная аутентификация")
                print(f"Повторная аутентификация для телефона {phone}")
                device_uuid = user['device_uuid']
                device_name = user['device_name']
                latitude = user['latitude']
                longitude = user['longitude']
                
                self.auth(phone, device_uuid, device_name, latitude, longitude)
