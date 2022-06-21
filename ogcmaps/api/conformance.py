import json

import requests

from ogcmaps.utils.urls import urls


class conformance:
    def __init__(self) -> None:

        self.conformance_urls = urls().conformance_urls()
        pass

    def metadata(self) -> dict:

        self.conformance_data = requests.get(
            self.conformance_urls["conformance_url"],
            headers=urls().json_headers,
        ).json()
        return json.dumps(self.conformance_data, indent=2)
