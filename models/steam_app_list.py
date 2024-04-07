from utils import requesthandler
from config import config

MAIN_KEY = 'steam_app_list'

def fetch_app_list():
    api_url = config.get_api_url(MAIN_KEY)
    response = requesthandler.make_api_request(api_url, None)
    fetch_data_items = []
    
    if response:
        fetch_data_items = response['applist']['apps']
    
        return fetch_data_items
    
    return None

def get_app_list_data_items():
    fetch_data_items = fetch_app_list()
    
    if fetch_data_items:
        columns = config.get_api_columns(MAIN_KEY)
        base_app_data = {key: None for key in columns}
        app_list_data_items = []
                
        for item in fetch_data_items:
            if item['name']:
                app_data = base_app_data.copy()
                
                for key in columns:
                    app_data[key] = item[key]
                        
                app_list_data_items.append(app_data)
        
        return app_list_data_items
    
    return None