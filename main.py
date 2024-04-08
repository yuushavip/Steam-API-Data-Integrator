from utils import csvhandler
from models import steam_app_list, steam_news, steam_appreviews, steam_appreviews_summary
import concurrent.futures

def fetch_and_write(func, file_name):
    data_items = func()
    
    if data_items:
        csvhandler.write_to_csv(data_items, file_name, 'w')

def main():
    all_fetch_functions = [
        (steam_app_list.get_app_list_data_items, 'steam_app_list.csv'),
        (steam_news.get_steam_news_data_items, 'steam_news_data.csv'),
        (steam_appreviews.get_steam_reviews_data_items, 'steam_reviews_data.csv'),
        (steam_appreviews_summary.get_steam_reviews_summary_data_items, 'steam_reviews_summary_data.csv')
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        
        for func, file_name in all_fetch_functions:
            future = executor.submit(fetch_and_write, func, file_name)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            
if __name__ == "__main__":
    main()