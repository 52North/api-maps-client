import requests


class maps:
    def __init__(self) -> None:

        self.keys = [
            "crs",
            "bbox",
            "width",
            "height",
            "cell-size",
            "transparent",
            "bgcolor",
            "datetime",
            "elevation",
            "f",
        ]
        pass

    def get_map(self, url, file_name, **kwargs) -> dict:

        for key, value in kwargs.items():
            if key in self.keys:
                pass
            else:
                return {"invalid parameter": key}

        query_string = "?" + "&".join(f"{key}={value}" for key, value in kwargs.items())
        endpoint = url + query_string
        map_data = requests.get(endpoint)
        file = open(f"{file_name}", "wb")
        file.write(map_data.content)
        file.close()

        return {"status": "success", "file name": f"{file_name}"}
