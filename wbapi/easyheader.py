import hmac
import hashlib
import time
import uuid
from typing import Dict
import platform

    
#android random device id
def generate_device_id() -> str:
    device_uuid = uuid.uuid4()
    return str(device_uuid)

#4.91.2 => 4910200
def version_to_number(version:str) -> int:
    parts = list(map(int, version.split('.')))
    
    while len(parts) < 4:
        parts.append(0)
        
    major = parts[0] * 1000000
    minor = parts[1] * 10000
    patch = parts[2] * 100
    build = parts[3] * 1
    
    return major + minor + patch + build

class SecurityInterceptor:
    #zapp-version: хардкор. SecurityInterceptor.smali => buildPayload()
    #zsignature_version - тоже хардкор SecurityInterceptor.smali => X-SIGNATURE-VERSION
    #zdevice_id и zdevice_name генерируются андроедом при каждой новой активации. рекомендую отдельно для каждого аккаунта отдельный айдишник.
    #zhmac_secret - опять хардкор. SecurityInterceptor => hmacSecretBytes_delegate
    def __init__(self, zapp_version:str, zsignature_version:str, zdevice_id:str="2340cdbf8163ee03", zdevice_name:str="huawei p30 pro", zhmac_secret:str = "18aaaabd-7299-4be8-a943-166a5fe0753f"):
        self.app_version = zapp_version #test on 4.91.2, константа SecurityInterceptor
        self.signature_version = zsignature_version #"6f8f8ea7-0773-4cde-a70e", константа SecurityInterceptor
        self.hmac_secret = zhmac_secret #константа SecurityInterceptor
        self.device_id = zdevice_id #must generate on every new account
        self.device_name = zdevice_name #must generate on every new account FROM EXISTING DEVICES LIST
        
    def _build_payload(self, timestamp: str, path: str) -> bytes:
        payload_string = f"{timestamp}{self.app_version}{path}"
        return payload_string.encode('utf-8')
    
    def _calculate_signature(self, payload: bytes) -> str:
        key = self.hmac_secret.encode('utf-8')
        hmac_obj = hmac.new(key, payload, hashlib.sha256)
        signature_bytes = hmac_obj.digest()
        
        return ''.join(f'{b:02x}' for b in signature_bytes)
    
    #website_host: хост (ex: courier-delivery-api.wildberries.ru)
    #path: путь до веба. ex: /api/v1/somepoebota
    #timestamp: unix time s
    #latitude: широта (координата)
    #longitude: долгота (координата)
    def generate_headers(self, website_host:str, path: str, latitude:float = 60.999999, longitude:float = 40.999999, timestamp: int = int(time.time())) -> Dict[str, str]:
        if timestamp is None:
            timestamp = int(time.time())
        
        timestamp_str = str(timestamp)
        
        payload = self._build_payload(timestamp_str, path)
        signature = self._calculate_signature(payload)
        
        headers = {
            "X-COORDINATES":f"{latitude}:{longitude}",
            "X-APP-VERSION": self.app_version,
            "X-APP-TYPE":"android", #а кто ещё?
            "DEVICE-ID":self.device_id,
            "DEVICE-NAME": self.device_name,
            "DEBUG":"false",
            "X-WB-COURIER-VERSION-NAME":self.app_version,
            "X-WB-COURIER-VERSION-CODE":str(version_to_number(self.app_version)),
            "X-WB-COURIER-VERSION-ANDROID-ID":self.device_id,
            "X-WB-COURIER-VERSION-IS-DEBUG":"false",
            "X-TIMESTAMP": timestamp_str,
            "X-SIGNATURE-VERSION": self.signature_version,
            "X-SIGNATURE": signature,
            "Host":website_host,
            "Connection": "Keep-Alive",
            "Accept-Encoding":"gzip",
            "User-Agent": "okhttp/4.12.0"
        }
        
        return headers


#example
# if __name__ == "__main__":
    # interceptor = SecurityInterceptor("4.91.2", "6f8f8ea7-0773-4cde-a70e")
    
    # test_path = "/api/v1/delivery/tasks-get-by-assignee"
    # fixed_timestamp = 1768837746
    # headers_fixed = interceptor.generate_headers(test_path, fixed_timestamp)
    
    # for key, value in headers_fixed.items():
        # print(f"{key}: {value}")