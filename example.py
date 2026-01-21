from wbapi.api import *

t_num = "78005553535"

def FindFreeTasksByCoords():
    api = WBCourierAPI()
    api.auth(t_num)
    inf = api.get_info(t_num)
    
    latitude = inf["latitude"]
    longitude = inf["longitude"]
    
    resp = api.request_with_query(
        t_num, 
        "GET", 
        "https://courier-delivery-api.wildberries.ru/api/v1/delivery/find-free-tasks-by-coords",
        {
            "lat":59.191479,
            "long":39.617294,
            "sm":""
        })
    
    print(resp.json())

def FindTaskByOffice():
    api = WBCourierAPI()
    api.auth(t_num)
    inf = api.get_info(t_num)
    latitude = inf["latitude"]
    longitude = inf["longitude"]
    
    resp = api.request_with_query(
        t_num, 
        "GET", 
        "https://courier-delivery-api.wildberries.ru/api/v1/delivery/find-free-tasks-by-office",
        {
            "office":"50133438",
            "sm":""
        })
    
    print(resp.json())

if __name__ == "__main__":
    FindFreeTasksByCoords()