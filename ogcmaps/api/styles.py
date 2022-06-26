import json

from ogcmaps.utils.components import maps
from ogcmaps.utils.urls import urls


class styles:
    def __init__(self) -> None:

        self.styles_urls = urls().styles_urls()
        pass

    def get_styled_map(self, style_id, file_name):

        get_styled_map_url = self.styles_urls["get_styled_map"].format(
            base_url=urls().base_url, styles=urls().styles, style_id=style_id
        )
        mapObj = maps()
        self.styled_map_data = mapObj.get_map(get_styled_map_url, file_name=file_name)
        return json.dumps(self.styled_map_data, indent=2)
