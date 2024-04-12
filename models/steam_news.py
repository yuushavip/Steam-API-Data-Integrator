from utils import requesthandler, confighandler
import concurrent.futures

MAIN_KEY = 'steam_news'

def fetch_steam_news(appid):
    url = confighandler.get_api_url(MAIN_KEY)
    params = confighandler.get_api_params(MAIN_KEY)
    params['appid'] = appid
    response = requesthandler.make_api_request(url, params)  
    fetch_data_items = []
        
    if response:
        fetch_data_items = response['appnews']['newsitems']
        
        return fetch_data_items
    
    return None

def get_steam_news_data(appid):
    fetch_data_items = fetch_steam_news(appid)
    news_data_items = []
    
    if fetch_data_items:
        columns = confighandler.get_api_columns(MAIN_KEY)
        base_news_data = {key: None for key in columns} 
        
        for item in fetch_data_items:
            news_data = base_news_data.copy()
            
            for key in columns:
                news_data[key] = item.get(key, None)
                
            news_data_items.append(news_data)
    
    return news_data_items

def get_steam_news_data_items():
    appids = confighandler.get_target_appids()
    news_data_items = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for appid in appids:
            future = executor.submit(get_steam_news_data, appid)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            new_data = future.result()
            news_data_items.extend(new_data)
                               
    return news_data_items