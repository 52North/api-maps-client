class urls:
    def __init__(
        self, response_format="?f=json", headers={"accept": "application/json"}
    ):
        self.format = response_format
        self.headers = headers
        self.base_url = "https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi"

        self.collections = f"/collections{self.format}"
        self.conformance = f"/conformance{self.format}"
        self.map = f"/map{self.format}"

        def base_url(self):
            return self.base_url + self.format

        def collections_url(self):
            return self.base_url + self.collections

        def conformance_url(self):
            return self.base_url + self.conformance

        def map_url(self):
            return self.base_url + self.map
