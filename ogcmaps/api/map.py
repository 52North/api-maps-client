import requests
from ..utils.urls import urls
from..utils.tojson import jsonify

class core:

  def __init__(self):
    self.map_urls = urls()

  def to_json(self):
    self.metadata = requests.get(self.map_urls.base_url).json()
    return jsonify(self.metadata)