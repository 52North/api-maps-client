import requests
from ..utils.urls import urls

class core:

  def __init__(self):
    self.map_urls = urls()

  def to_json(self):
    self.metadata = requests.get(self.map_urls.base_url)
    return self.metadata