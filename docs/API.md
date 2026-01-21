# You can find wildberries' requests by strings 'END_POINT' 'Lretrofit2/http/'

Files: [AuthApi.smali, ActApi.smali, LogOutApi.smali, OrrAuthApi.smali, AutoAssigmentApi.smali, BalanceApi.smali, BeginnerBonusApi, ClientChatApi.smali, CompanyApi.smali, CourierDeliveryApi.smali]


Authtorization Bearer <==

Headers:
X-COORDINATES: 15.752004:97.617734 
X-APP-VERSION 4.91.2 
X-APP-TYPE: android 
DEVICE-ID: 2340cdbf8163ee03 
DEVICE-NAME: huawei p30 pro 
DEBUG: false 
X-WB-COURIER-VERSION-NAME: 4.91.2 
X-WB-COURIER-VERSION-CODE: 4910200 
X-WB-COURIER-VERSION-ANDROID-ID: 2340cdbf8163ee03 
X-WB-COURIER-VERSION-IS-DEBUG: false 
X-TIMESTAMP: 1768837746 
X-SIGNATURE-VERSION: 12348ea7-0773-4cde-a70e 
X-SIGNATURE: 1234e24133021894923b406a31e8fd87d7ca2166397e9f3fea7962fc7224
Authorization: Bearer TOKENTOKENTOKENTOKENTOKENTOKENTOKEN

Connection: Keep-Alive 
Accept-Encoding: gzip 
User-Agent: okhttp/4.12.0



# Warn: Лучше всего найти в исходниках эти строки и посмотреть как их использовать. Аккаунт могут убить или ещё что похуже

??? Означает или есть данные или нет

BODY: ??? Означает что тип данных точно BODY, но неизвестно что в нём. МОЖНО ОТКОПАТЬ

NONE Означает что данных кроме хедеров нет

Accept: application/json, text/plain

Content-Type: application/json

# [https://courier.wb.ru/mobile-api/](https://example.com/) (MOBILE_API_END_POINT)

AUTH-GET: api/v1/cities/search, QUERY: country=&query=

AUTH-GET: api/v1/courier/acts/list, ???

AUTH-POST: api/v1/courier/acts/accept, ???

AUTH-GET: api/v1/bonus/get, ???

AUTH-GET: api/v1/education/portal-authorized, ???

AUTH-POST: api/v2/partners/courier_add, BODY: ???

AUTH-GET: api/v1/kisart/courier/status, ???

AUTH-GET: api/v1/courier/profile, ???

AUTH-GET: api/v1/referral, ???

AUTH-GET: api/v1/call-center/file/download, Header: fileID

AUTH-GET: api/v1/call-center/message/get, QUERY: lp=&delay=&message_id&enter_chat=

AUTH-POST: api/v1/call-center/file/upload, MULTIPART; Header: RecipientID

AUTH-POST: api/v1/call-center/message/send, BODY: ???

# [https://x-courier-api.wildberries.ru/](https://example.com/) (REG_COMPANY_END_POINT)

AUTH-GET: api/v1/courier/acts/list, ???

AUTH-POST: api/v1/courier/offer/accept, BODY: ???

AUTH-POST: api/v1/partners/courier_ban, BODY: ???

AUTH-POST: api/v1/npd/bind, BODY: ???

GET: api/v1/calculator, QUERY: weight=&metres=&deliveries=&days=&increased=&city=

AUTH-POSY: api/v1/npd/cancel-income, BODY: ???

AUTH-POST: api/v1/profile/change-phone/confirm-phone, QUERY: code=

AUTH-POST: api/v1/profile/change-phone/confirm-new-phone, QUERY: code=&phone=

AUTH-POST: api/v1/partners/courier_edit, BODY: ???

GET: api/v1/banks/by-bic/{BIC}, PATH: BIC

AUTH-GET: api/v1/courier/view/favorite-office/find, QUERY: search_text=&region_name=

GET: api/v1/agreements, QUERY: own_type=

AUTH-GET: api/v1/motivation/balance, ???

AUTH-GET: api/v1/courier/user-info/bank-account, QUERY: country=

AUTH-GET: api/v1/partners/couriers, ???

AUTH-GET: api/v1/partners/profile, ???

AUTH-GET: api/v1/profile/reviews, ???

AUTH-GET: api/v1/admin/courier/reviews, QUERY: wb_courier_id=

AUTH-GET: api/v2/motivation/payslip, QUERY: from=&to=

GET: api/v1/calculator/options, ???

AUTH-GET: api/v1/npd/cancel-income-reasons, ???

AUTH-GET: api/v1/courier/user-info/request/last-change-user-info, ???

AUTH-GET: api/v1/courier/user-info/favorite-office, NONE

AUTH-GET: api/v1/npd/account-status, ???

AUTH-GET: api/v1/courier/office-regions, ???

AUTH-GET: api/v1/courier/view/favorite-office/all, ???

AUTH-GET: api/v1/register_partner/status, ???

AUTH-GET: api/v1/courier/user-info, ???

AUTH-GET: api/v1/profile/change-phone, ???

AUTH-GET: api/v1/npd/incomes, ???

AUTH-GET: api/v1/npd/status, NONE

AUTH-GET: api/v1/tags/my, ???

AUTH-GET: api/v1/couriers/default-upgrade-info, ???

AUTH-GET: api/v1/motivation/withdrawal-requests/details, QUERY: tx_id=

AUTH-GET: api/v1/motivation/withdrawal-requests/details, QUERY: from=&to=

AUTH-POST: api/v1/courier/user-info/favorite-office/add, BODY: ???

AUTH-POST: api/v1/courier/ping, BODY: ???

AUTH-POST: api/v1/courier/user-info/favorite-office/delete, BODY: ???

AUTH-GET: api/v1/profile/change-phone/get-code, ???

AUTH-POST: api/v1/profile/change-phone/set-new-phone, QUERY: phone=

AUTH-POST: api/v1/motivation/request-withdraw, QUERY: amount=

AUTH-GET: api/v1/admin/courier/find, QUERY: findStr=

AUTH-GET: api/v1/courier/view/favorite-office/search, QUERY: search_text=

AUTH-GET: api/v1/courier/region-search, QUERY: search_text=

Content-Type: image/jpeg

AUTH-POST: api/v1/courier/avatar-upload, BODY: ???

AUTH-POST: api/v1/courier/upload-delivery-photo, MULTIPART: ???

Content-Type: application/json

AUTH-GET: api/v1/self-employed/money-transfer/{moneyTranId}/receipt, PATH: moneyTranId

AUTH-POST: api/v1/courier/change-mobility-type, BODY: ???

AUTH-POST: api/v1/courier/region-set, BODY: ???

AUTH-POST: api/v1/courier/offer/terminate, ???

AUTH-POST: api/v1/partners/courier_unban, BODY: ???

AUTH-POST: api/v2/courier/user-info/bank-account, BODY: ???

AUTH-POST: api/v1/courier/user-info, BODY: ???

AUTH-POST: api/v2/courier/user-info, ???

AUTH-POST: api/v1/photo_register/change-type-to-smz, ???

AUTH-GET: api/v1/photo_register/status, ???

AUTH-GET: api/v1/register_partner/status, ???

AUTH-POST: api/v1/photo_register/register, BODY: ???

AUTH-POST: api/v1/photo_register/fixed, BODY: ???

AUTH-POST: api/v1/register_partner/fixed, BODY: ???

AUTH-POST: api/v1/register_partner/register, BODY: ???

AUTH-POST: api/v1/{reg_type}/upload_photo, MULTIPART; PATH: reg_type

AUTH-POST: api/v1/photo_register/fixed_td, BODY: ???

AUTH-POST: api/v2/photo_register/register_td, BODY: ???

AUTH-POST: api/v1/notifications/delete, BODY: ???

AUTH-POST: api/v1/npd/notifications/archive, BODY: ???

AUTH-GET: api/v1/notifications, NONE

AUTH-GET: api/v1/npd/notifications?read=true&archived=false, NONE (да, Тут прям в коде Query)

AUTH-GET: api/v1/npd/notifications/count, ???

AUTH-POST: api/v1/notifications/mark-read, BODY: ???

AUTH-POST: api/v1/npd/notifications/read, BODY: ???

AUTH-POST: api/v1/notifications/set-fcm-token, BODY: {fcm_token:str}

AUTH-POST: api/v1/notifications/set-hpk-token, BODY: ???

БЛЯТ ГОСУСЛУГИ

AUTH-POST: api/v1/esia/register, BODY: ???

AUTH-POSY: api/v1/esia/start_customs, ???

AUTH-POST: api/v1/esia/verify, BODY: ???

GET: api/v1/couriers/app/flags, NONE

AUTH-GET: api/v1/courier/personal_agreements, ???

AUTH-POST: api/v1/courier/personal_agreements/accept, BODY: ???

GET: api/live, None (ping)

# [https://r-point.wb.ru/wbc/api/v1/](https://example.com/) (AUTH_API_END_POINT)

POST: courier/validate, BODY: {token:required,code:required}

POST: login, BODY: {phone:required}

POST: courier/refresh, BODY: {token:required} ?auth?

POST: logout, BODY: {"deviceType":"DEVICE_ANDROID"} !!AUTH!!

# [https://auth-orr.wildberries.ru/](https://example.com/) (OLD_AUTH_API_END_POINT)

Content-Type: application/x-www-form-urlencoded

AUTH-GET: request_code, QUERY: phone=

CLIENT-POST: connect/token, FIELD: {grant_type, scope, username, password}

CLIENT-POST: connect/token, FIELD: {grant_type, refresh_token}

# [https://courier-delivery-api.wildberries.ru](https://example.com/) (COURIER_DELIVERY_API_END_POINT)

AUTH-POST: api/v1/delivery/task-assign, BODY: ???

AUTH-POST: api/v1/delivery/postpayment, BODY: ???

AUTH-POST: api/v1/delivery/postponement, BODY: ???

AUTH-POST: api/v1/dial/makecall-to-user, BODY: ???

AUTH-GET: api/v1/geotracking/get-events, QUERY: id=&from=&to=

AUTH-GET: api/v1/delivery/tasks-get-by-assignee, QUERY: id=

AUTH-GET: api/v1/delivery/tasks-get-completed, QUERY: id=&from=&to=

AUTH-GET: api/v1/delivery/check-postpayment-status/{deliveryUid}, PATH: deliveryUid

AUTH-POST: api/v2/delivery/check-postpayment-status, BODY: ???

AUTH-GET: api/v1/delivery/find-free-tasks-by-coords, QUERY: lat=&long=&sm=; (sm is empty) Header: view=simplify

AUTH-GET: api/v2/delivery/find-free-tasks-by-coords, QUERY: lat=&long=&sm=; (sm is empty) Header: view=simplify

AUTH-GET: api/v1/dict/user-rate-reasons, ???

AUTH-GET: api/v1/delivery/pretension/{id}, PATH: id

AUTH-GET: api/v1/delivery/defect-type, ???

AUTH-GET: api/v1/geotracking/get-events, QUERY: from=&to=

AUTH-GET: api/v1/dict/appointment-cancellation-reasons, ???

AUTH-GET: api/v1/delivery/task/{taskUid}, PATH: taskUid

AUTH-GET: api/v1/delivery/find-free-tasks-by-office, QUERY: office=&sm=; Header: view

AUTH-POST: api/v1/delivery/inventory-status-set, BODY: ???

AUTH-POST: api/v1/delivery/rate-user, BODY: ???

AUTH-POST: api/v1/delivery/register, BODY: ???

AUTH-POST: api/v2/delivery/task-cancel-assignment, MULTIPART: data

AUTH-POST: api/v1/delivery/wh-hand-off, BODY: ???

AUTH-GET: api/v1/delivery/tasks-get-by-assignee, Header: View

AUTH-POST: api/v1/geotracking/save-event, BODY: ???

AUTH-POST: api/v1/delivery/fitting, BODY: ???

AUTH-POST: api/v1/delivery/wh-tare, BODY: ???

AUTH-POST: api/v2/delivery/inventory-status-set, MULTIPART: data

AUTH-POST: api/v1/delivery/set-visit-info, BODY: ???

AUTH-POST: api/v1/delivery/task-change-status, BODY: ???

AUTH-GET: api/v1/delivery/tasks-get-by-assignee, NONE <=====

AUTH-GET: api/v1/delivery/tasks-get-completed, Header: view

AUTH-GET: api/v1/delivery/tasks-get-completed, Query: from=&to=

AUTH-GET: api/v1/delivery/tasks-get-completed, Query: shk=; Header: view

AUTH-POST: api/v1/delivery/comment-add, BODY: ???

# [https://heritage.wildberries.ru](https://example.com/) (HERITAGE_API_END_POINT)

AUTH-GET: v1/proxy/basket-shards/shardes_v2, ???

# [https://wbc-metrics.wb.ru/](https://example.com/) (ANALYTICS_V2_API_END_POINT)

POST: api/v1/events, BODY: ???; TAG: ???

# [https://courier.wb.ru/delivery-stats/](https://example.com/) (COURIER_STATS_API_END_POINT)

AUTH-GET: v1/transactions/couriers, QUERY: date_from=&date_to=&page=&page_size=

# [https://courier.wb.ru/rating/](https://example.com/) (RATING_END_POINT)

AUTH-GET: v1/rating/courier, ???

# [https://courier-balance.wildberries.ru/](https://example.com/) (BALANCE_API_END_POINT)

AUTH-POST: api/v1/balance/withdraw, BODY: ???

AUTH-GET: api/v1/balance, BODY: ???

AUTH-GET: api/v1/balance/get-payment-banking-details, BODY: ???

AUTH-GET: api/v1/transactions, QUERY: date_from=&date_to=&offset=&type=&

AUTH-GET: api/v1/balance/withdrawable-amount, BODY ???

# [https://point-search.wb.ru/](https://example.com/) (HELPER_CHAT_API_END_POINT)

AUTH-POST, bert-api/delivery/send-message, BODY: ???

# [https://courier.wb.ru/stories/](https://example.com/) (STORIES_API_END_POINT)

AUTH-POST: v3/stories, BODY: ???

AUTH-GET: v2/{story_id}/{slide_id}/{action}, PATH: story_id,slide_id,action

# [https://courier.wb.ru/tickets/](https://example.com/) (TICKETS_API_END_POINT)

POST: v1/ticket/bot-button-click, BODY: ???

AUTH-POST: v1/ticket/set-status, BODY: ???

AUTH-POST: v2/ticket/create, BODY: ???

AUTH-POST: v1/ticket/create-message, BODY: ???

AUTH-GET: v2/ticket/get/{id}, PATH: id

AUTH-GET: v2/tickets/categories, QUERY: is_allow_work=

AUTH-GET: v1/tickets/available-challenge-reasons, ???

AUTH-POST: v2/ticket/get-all, BODY: ???; Header: application/json

AUTH-POST: v1/tickets/uploadfiles, MULTIPART

# [https://x-lost-shk.wildberries.ru/](https://example.com/) (SHORTAGE_END_POINT)

AUTH-GET: api/v1/losses/get, QUERY: subject=

AUTH-GET: api/v1/losses/info/{id}, PATH: id

AUTH-GET: api/v1/losses/available-groups, ???

AUTH-GET: api/v1/losses/get, QUERY: employee=

AUTH-POST: api/v1/losses/discuss, BODY: ???

# [https://courier.wb.ru/autoassignment/](https://example.com/) (AUTOASSIGNMENT_API_END_POINT)

AUTH-POST: api/v1/offline, BODY: {fcm_token:str,lat:null,long:null} //3

AUTH-POST: api/v1/online, BODY: {fcm_token:str,lat:double,long:double} //1

AUTH-POST: api/v1/line-status, BODY: {fcm_token:str,lat:double,long:double}

AUTH-POST: api/v1/autoassignment/event, BODY: {delay:int} //2

# [https://chat.wildberries.ru/api/courier-chat-srv/](https://example.com/) (CLIENT_CHAT_API_END_POINT)

AUTH-GET: v1/courier/chats, ???

AUTH-POST: v1/courier/history, BODY: ???

AUTH-POST: v1/courier/events, BODY: ???

AUTH-POST: v1/courier/unread, BODY: ???

AUTH-POST: v1/courier/send, BODY: ???

AUTH-POST: v1/courier/upload, Header {recipientID,Content-Type,file}

AUTH-POST: v1/courier/validation, BODY: ???

# [https://tutwifi.ru/](https://tutwifi.ru/) (WI_FI_POINTS_API_END_POINT)

НЕ ВАЛБЕРИС

GET: api/points, QUERY: limit=&offset=

# Неответы:

POST: api/v1/courier/user-info/cancel-vacancy-request

GET: api/v1/motivation/cis-payments

GET: api/v1/entrepreneurs/shortages/details?shortage_id=1

GET: api/v1/entrepreneurs/shortages?

GET: api/v1/profile/debts/details?docType=1&docGuid=1

GET: api/v1/profile/debts

GET: api/v1/courier/decline-offices?region=Москва

GET: api/v1/vacancies/action-log

POST: api/v1/entrepreneurs/profile/phone

POST: api/v1/courier/user-info/vacancy-report
