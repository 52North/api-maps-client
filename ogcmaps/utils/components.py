def uri(url, keys, **kwargs) -> dict:

    for key, value in kwargs.items():
        if key in keys:
            pass
        else:
            return {"invalid parameter": key}

    query_string = "?" + "&".join(f"{key}={value}" for key, value in kwargs.items())
    endpoint = url + query_string

    return {"endpoint": endpoint}
