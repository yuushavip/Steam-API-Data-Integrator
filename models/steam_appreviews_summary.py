from config import config
from utils import requesthandler
import concurrent.futures
import time

MAIN_KEY = 'steam_appreviews_summary'

def fetch_steam_reviews_summary(appid):
    url = f"{config.get_api_url(MAIN_KEY)}{appid}"
    params = config.get_api_params(MAIN_KEY)
    response = requesthandler.make_api_request(url, params)

    return response['query_summary']

def get_steam_reviews_summary_data(appid):
    fetch_data_items = fetch_steam_reviews_summary(appid)
    reviews_summary_data_items = []
    
    if fetch_data_items:
        columns = config.get_api_columns(MAIN_KEY)
        base_reviews_summary_data = {key: None for key in columns}
        current_timestamp = int(time.time())
        
        summary_data = base_reviews_summary_data.copy()
        summary_data['date'] = current_timestamp
        summary_data['appid'] = appid
            
        for key in columns:
            summary_data[key] = fetch_data_items[key]
                
        reviews_summary_data_items.append(summary_data)
    
    return reviews_summary_data_items

def get_steam_reviews_summary_data_items():
    appids = config.get_target_appids()
    reviews_summary_data_items = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for appid in appids:
            future = executor.submit(get_steam_reviews_summary_data, appid)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            new_data = future.result()
            reviews_summary_data_items.extend(new_data)
    
    return reviews_summary_data_items