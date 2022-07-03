import json

import requests

from ogcmaps.utils.components import maps
from ogcmaps.utils.urls import urls


class collections:
    def __init__(self) -> None:

        self.collections_urls = urls().collections_urls()
        pass

    def metadata(self) -> dict:

        self.collections_data = requests.get(
            self.collections_urls["collections_url"],
            headers=urls().json_headers,
        ).json()
        return json.dumps(self.collections_data, indent=2)

    def get_collection(self, collection_id) -> dict:

        get_collection_url = self.collections_urls["get_collection"].format(
            base_url=urls().base_url,
            collections=urls().collections,
            collection_id=collection_id,
        )
        self.get_collection_data = requests.get(
            get_collection_url, headers=urls().json_headers
        ).json()
        return json.dumps(self.get_collection_data, indent=2)

    def get_collection_map(self, collection_id, file_name, **kwargs) -> dict:

        get_collection_map_url = self.collections_urls["get_collection_map"].format(
            base_url=urls().base_url,
            collections=urls().collections,
            collection_id=collection_id,
        )
        mapObj = maps()
        self.map_image_data = mapObj.get_map(
            get_collection_map_url, file_name=file_name, **kwargs
        )
        return json.dumps(self.map_image_data, indent=2)

    def get_collection_styles(self, collection_id) -> dict:

        get_collection_styles_url = self.collections_urls[
            "get_collection_styles"
        ].format(
            base_url=urls().base_url,
            collections=urls().collections,
            collection_id=collection_id,
        )
        self.collection_styles = requests.get(
            get_collection_styles_url, headers=urls().json_headers
        ).json()
        return json.dumps(self.collection_styles, indent=2)

    def get_collection_style(self, collection_id, style_id) -> dict:

        get_collection_style_url = self.collections_urls["get_collection_style"].format(
            base_url=urls().base_url,
            collections=urls().collections,
            collection_id=collection_id,
            style_id=style_id,
        )
        self.collection_style = requests.get(
            get_collection_style_url, headers=urls().json_headers
        ).json()
        return json.dumps(self.collection_style, indent=2)