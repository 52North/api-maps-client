import requests


def uri(url, keys, **kwargs) -> dict:

    for key, value in kwargs.items():
        if key in keys:
            pass
        else:
            raise ValueError({"Invalid parameter": f"{key}"})

    query_string = "?" + "&".join(f"{key}={value}" for key, value in kwargs.items())
    endpoint = url + query_string

    return {"endpoint": endpoint}


def write(endpoint, file_name) -> dict:

    map_data = requests.get(endpoint["endpoint"], headers={"accept": "image/png"})
    file = open(f"{file_name}", "wb")
    file.write(map_data.content)
    file.close()

    return {"status": "success", "file name": f"{file_name}"}
