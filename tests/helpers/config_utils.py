import os
import yaml


def get_config():
    with open('tests/config/environment.yaml') as file:
        local_config = yaml.full_load(file)
    environment = os.getenv('ENVIRONMENT', 'local')
    return local_config[environment]


cfg = get_config()
