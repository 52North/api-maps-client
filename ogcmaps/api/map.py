import json

import requests

from ..utils.urls import urls


class core:
    def __init__(self):
        self.map_urls = urls()

    def metadata(self):
        self.metadata = requests.get(self.map_urls.base_url).json()
        return json.dumps(self.metadata, indent=2)
