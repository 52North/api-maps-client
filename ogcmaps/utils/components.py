import importlib
import inspect
from pprint import pformat

import requests
import requests_cache

requests_cache.install_cache(
    "ogcmaps.cache", backend="sqlite", expire_after=180, use_temp=True
)


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

    return {"status": "success", "fileName": f"{file_name}"}


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


def is_mod_function(mod, func):
    "checks that func is a function defined in module mod"
    return inspect.isfunction(func) and inspect.getmodule(func) == mod


def get_funcs(mod_list):

    rv = []
    for mod in mod_list:
        mod_func = importlib.import_module("ogcmaps." + mod)
        for func in mod_func.__dict__.values():
            if is_mod_function(mod_func, func):
                if func.__name__ == "metadata":
                    rv.append(f"{mod}_{func.__name__}")
                else:
                    rv.append(func.__name__)
    rv.sort()
    return rv


def printer(ctx, obj):

    if ctx.obj["pretty_print"]:
        return pformat(obj, indent=2)
    else:
        return obj


def parse_options(ctx):
    return {ctx.args[i][2:]: ctx.args[i + 1] for i in range(0, len(ctx.args), 2)}
