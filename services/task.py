from utils import csvhandler
from models import steam_app_list, steam_news, steam_appreviews, steam_appreviews_summary
import concurrent.futures

def fetch_steam_data_and_save_to_csv(func, file_name):
    print(f'Starting to fetch data and save to {file_name}...')
    
    data_items = func()
    csvhandler.write_to_csv(data_items, file_name, 'w')
    
    print(f'Finished fetching data and saved to {file_name}')
        
    return data_items

def fetch_all_steam_data_and_save_to_csv():
    all_fetch_functions = [
        (steam_app_list.get_app_list_data_items, 'steam_app_list.csv'),
        (steam_news.get_steam_news_data_items, 'steam_news_data.csv'),
        (steam_appreviews.get_steam_reviews_data_items, 'steam_reviews_data.csv'),
        (steam_appreviews_summary.get_steam_reviews_summary_data_items, 'steam_reviews_summary_data.csv')
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        file_names = {}
        
        for func, file_name in all_fetch_functions:
            future = executor.submit(fetch_steam_data_and_save_to_csv, func, file_name)
            futures.append(future)
            file_names[future] = file_name

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            file_name = file_names[future]
            
            print(f'Completely processed {file_name}')
    
    return result