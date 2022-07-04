from ogcmaps.utils.components import maps
from ogcmaps.utils.urls import urls

styles_urls = urls().styles_urls()


def get_styled_map(style_id, file_name):

    get_styled_map_url = styles_urls["get_styled_map"].format(
        base_url=urls().base_url, styles=urls().styles, style_id=style_id
    )
    mapObj = maps()
    styled_map_data = mapObj.get_map(get_styled_map_url, file_name=file_name)
    return styled_map_data
