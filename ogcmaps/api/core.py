import json

import requests

from ogcmaps.utils.urls import urls


class core:
    def __init__(self) -> None:

        self.core_urls = urls().core_urls()
        pass

    def metadata(self) -> dict:

        self.core_data = requests.get(
            self.core_urls["core_url"], headers=urls().json_headers
        ).json()
        return json.dumps(self.core_data, indent=2)
