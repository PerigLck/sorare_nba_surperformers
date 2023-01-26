import json

def get_config(config_path):
    """_read config in json et return dict_

    Args:
        config_path (_string_): _config_path_

    Returns:
        _dict_: _conf dict_
    """
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data