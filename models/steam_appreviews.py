from utils import requesthandler, confighandler
import concurrent.futures

MAIN_KEY = 'steam_appreviews'

def fetch_steam_reviews(appid, cursor=None):
    url = f"{confighandler.get_api_url(MAIN_KEY)}{appid}"
    params = confighandler.get_api_params(MAIN_KEY)
        
    if cursor:
        params['cursor'] = cursor.encode()
            
    response = requesthandler.make_api_request(url, params)

    return response

def fetch_all_steam_reviews(appid):
    all_reviews = []
    cursor = "*"  # Initial cursor value

    while True:
        response = fetch_steam_reviews(appid, cursor=cursor)

        if not response or response.get("success") != 1:
            break

        if response['query_summary']['num_reviews'] == 0:
            break

        all_reviews.extend(response["reviews"])

        if response.get("cursor"):
            cursor =  response["cursor"]
        else:
            break

    return all_reviews

def get_steam_reviews_data(appid):
    columns = confighandler.get_api_columns(MAIN_KEY)
    all_reviews_json = fetch_all_steam_reviews(appid)
    base_review_data = {key: None for key in columns}
    review_data_items = []

    for item in all_reviews_json:
        review_data = base_review_data.copy()
        review_data['appid'] = appid
        item_author = item['author']
        
        for key in columns:
            if key.startswith("author_"):
                item_key = key.replace("author_", "")
                review_data[key] = item_author.get(item_key, None)
            else:
                review_data[key] = item.get(key, None)

        review_data_items.append(review_data)

    return review_data_items

def get_steam_reviews_data_items():
    appids = confighandler.get_target_appids()
    review_data_items = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for appid in appids:
            future = executor.submit(get_steam_reviews_data, appid)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            review_data = future.result()
            review_data_items.extend(review_data)

    return review_data_items