import yaml
import os

def get_config_file(main_key):
    file_name = 'config.yaml'
    file_path = f"config/{file_name}"
    
    if os.environ.get('CONFIG_DIR_PATH'):
        file_path = f"{os.environ['CONFIG_DIR_PATH']}{file_name}"
    
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    
    api_config = config.get(main_key, {})
    
    return api_config

def get_target_appids():
    config = get_config_file('settings')
    target_appids = config.get('target_appids', {})
    
    return target_appids

def get_api_url(main_key):
    config = get_config_file(main_key)
    api_url = config.get('api_url', {})
    
    return api_url

def get_api_columns(main_key):
    config = get_config_file(main_key)
    columns = config.get('columns', {})
    
    return columns

def get_api_params(main_key):
    config = get_config_file(main_key)
    params = {}
    
    if config:
        params_config = config.get('params', {})
        
        for key, value in params_config.items():
            if value:
                params[key] = value

    return params