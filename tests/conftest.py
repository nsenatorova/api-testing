import os

import yaml


def get_url():
    directory = os.path.join(os.path.dirname(__file__), '../config/config.yml')
    with open(directory) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    url = data['url']
    return url
