class urls:
    def __init__(
        self, response_format="?f=json", headers={"accept": "application/json"}
    ):
        self.format = response_format
        self.headers = headers
        self.base_url = (
            "https://virtserver.swaggerhub.com/UAB-CREAF/"
            "ogc-api-maps-opf-xmp-more-1-collection/1.0.0/"
        )

        self.collections = "collections"
        self.conformance = "conformance"
        self.map = "map"

    def core_urls(self) -> dict:
        return {"core_url": self.base_url + self.format, "headers": self.headers}

    def collections_urls(self) -> dict:
        return {
            "collections_url": self.base_url + self.collections + self.format,
            "headers": self.headers,
        }

    def conformance_urls(self) -> dict:
        return {
            "conformance_url": self.base_url + self.conformance + self.format,
            "headers": self.headers,
        }

    def map_urls(self) -> dict:
        return {
            "map_url": self.base_url + self.map + self.format,
            "headers": self.headers,
        }
