def get_config():
    file = 'config.ini'
    config = {}
    with open(file, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.split("=")
                config[key.strip()] = value.strip()
    return config

def get_username():
    return get_config()["LEETCODE_USERNAME"]

def get_cv_filename():
    return get_config()["CV_FILENAME"]