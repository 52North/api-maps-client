class urls:
    def __init__(self):

        self.base_url = "https://maps.ecere.com/ogcapi/"

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
            "/{collection_id}/map/tiles/{tile_matrix_set_id}/{tile_matrix}/"
            "{tile_row}/{tile_col}",
            "get_collection_styled_tiles": "{base_url}{collections}"
            "/{collection_id}/styles/{style_id}/map/tiles",
            "collection_styled_map_tile_matrix": "{base_url}{collections}"
            "/{collection_id}/styles/{style_id}/map/tiles/{tile_matrix_set_id}",
            "collection_styled_map_tile": "{base_url}{collections}"
            "/{collection_id}/styles/{style_id}/map/tiles/{tile_matrix_set_id}/"
            "{tile_matrix}/{tile_row}/{tile_col}.{f}",
        }

    def conformance_urls(self) -> dict:

        return {
            "conformance_url": self.base_url + self.conformance,
        }

    def map_urls(self) -> dict:

        return {
            "map_url": self.base_url + self.map,
            "get_map_tiles": self.base_url + self.map + "/tiles",
            "map_tile_matrix_set": "{base_url}{map}/tiles/{tile_matrix_set_id}",
            "get_map_tile": "{base_url}{map}/tiles/{tile_matrix_set_id}"
            "/{tile_matrix}/{tile_row}/{tile_col}",
        }

    def styles_urls(self) -> dict:

        return {
            "get_styled_map": "{base_url}{styles}/{style_id}/map",
            "get_styled_map_tiles": "{base_url}{styles}/{style_id}/map/tiles",
            "get_styled_map_tiles_matrix": "{base_url}{styles}/{style_id}/map/tiles/"
            "{tile_matrix_set_id}",
            "get_styled_map_tile": "{base_url}{styles}/{style_id}/map/tiles/"
            "{tile_matrix_set_id}/{tile_matrix}/{tile_row}/{tile_col}",
        }
