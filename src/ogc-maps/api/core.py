import requests
from ..utils.urls import urls

class core:

  def __init__(self):
    self.map_urls = urls()
    response = requests.get(self.map_urls.base_url)
    return response
