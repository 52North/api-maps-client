import requests

from ogcmaps.utils.components import uri
from ogcmaps.utils.urls import urls

styles_urls = urls().styles_urls()


def get_styled_map(style_id, file_name, **kwargs):

    keys = [
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

    get_styled_map_url = styles_urls["get_styled_map"].format(
        base_url=urls().base_url, styles=urls().styles, style_id=style_id
    )

    endpoint = uri(get_styled_map_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        map_data = requests.get(endpoint["endpoint"])
        file = open(f"{file_name}", "wb")
        file.write(map_data.content)
        file.close()
        return {"status": "success", "file name": f"{file_name}"}

    return endpoint
