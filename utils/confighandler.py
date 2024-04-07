import configparser

def get_config(file_name):
    config = configparser.ConfigParser()
    config.optionxform = str
    
    if configparser.environ.get('CONFIG_DIR_PATH'):
        config_path_dir = configparser.environ['CONFIG_DIR_PATH']
        config.read(f"{config_path_dir}{file_name}")
    else:
        config.read(file_name, encoding='utf-8')
    
    return config