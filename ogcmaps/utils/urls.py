class urls:
    def __init__(self):

        self.json_headers = {"accept": "application/json"}
        self.base_url = "https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa/"

        self.collections = "collections"
        self.conformance = "conformance"
        self.map = "map"

    def core_urls(self) -> dict:

        return {"core_url": self.base_url}

    def collections_urls(self) -> dict:

        return {
            "collections_url": self.base_url + self.collections,
            "get_collection": "{base_url}{collections}/{id}",
            "get_collection_map": "{base_url}{collections}/{id}/map",
        }

    def conformance_urls(self) -> dict:

        return {
            "conformance_url": self.base_url + self.conformance,
        }

    def map_urls(self) -> dict:

        return {
            "map_url": self.base_url + self.map,
        }
