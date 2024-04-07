from utils import requesthandler

def get_keys():
    return ["appid", "name"]
    
def fetch_app_list():
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requesthandler.make_api_request(url, None)
    fetch_data_items = response['applist']['apps']
    
    if not fetch_data_items:
        return None
    
    return fetch_data_items

def get_app_list_data_items():
    fetch_data_items = fetch_app_list()
    
    if not fetch_data_items:
        return None
    
    base_app_data = {key: None for key in get_keys()}
    app_list_data_items = []
            
    for item in fetch_data_items:
        if item['name']:
            app_data = base_app_data.copy()
            app_data.update({
                'appid': item['appid'],
                'name': item['name']
            })
                    
            app_list_data_items.append(app_data)
        
    return app_list_data_items