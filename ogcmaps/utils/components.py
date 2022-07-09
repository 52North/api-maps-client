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


def write_image(endpoint, file_name, f) -> dict:

    map_data = requests.get(endpoint["endpoint"], headers={"accept": f"image/{f}"})
    file = open(f"{file_name}", "wb")
    file.write(map_data.content)
    file.close()

    return {"status": "success", "file name": f"{file_name}"}


def get_data(endpoint, response_format):

    if response_format == "json":
        raw_data = requests.get(
            endpoint, headers={"accept": f"application/{response_format}"}
        )
        return raw_data.json()

    elif response_format == "html":
        html_endpoint = (
            endpoint + "&f=html" if ("?" in endpoint) else endpoint + "?f=html"
        )
        raw_data = requests.get(html_endpoint)
        return raw_data.text
