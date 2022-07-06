class urls:
    def __init__(self):

        self.json_headers = {"accept": "application/json"}
        self.base_url = "https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa/"

        self.collections = "collections"
        self.conformance = "conformance"
        self.map = "map"
        self.styles = "styles"

    def landing_urls(self) -> dict:

        return {"landing_url": self.base_url}

    def collections_urls(self) -> dict:

        return {
            "collections_url": self.base_url + self.collections,
            "get_collection": "{base_url}{collections}/{collection_id}",
            "get_collection_map": "{base_url}{collections}/{collection_id}/map",
            "get_collection_styles": "{base_url}{collections}/{collection_id}/styles",
            "get_collection_style": "{base_url}{collections}"
            "/{collection_id}/styles/{style_id}",
            "get_collection_styled_map": "{base_url}{collections}"
            "/{collection_id}/styles/{style_id}/map",
            "get_collection_map_tiles": "{base_url}{collections}"
            "/{collection_id}/map/tiles",
            "get_collection_map_tile_matrix": "{base_url}{collections}"
            "/{collection_id}/map/tiles/{tile_matrix_set_id}",
            "get_collection_map_tile": "{base_url}{collections}"
            "/{collection_id}/map/tiles/{tile_matrix_set_id}/{tile_matrix}"
            "{tile_row}/{tile_col}",
        }

    def conformance_urls(self) -> dict:

        return {
            "conformance_url": self.base_url + self.conformance,
        }

    def map_urls(self) -> dict:

        return {
            "map_url": self.base_url + self.map,
        }

    def styles_urls(self) -> dict:

        return {"get_styled_map": "{base_url}{styles}/{style_id}/map"}
