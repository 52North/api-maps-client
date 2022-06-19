class urls:

  def __init__(self, response_format="?f=json"):
    self.format = response_format
    self.base_url = "https://maps.ecere.com/"

    self.collections = f"collections{self.format}"
    self.conformance = f"conformance{self.format}"
    self.map = f"map{self.format}"

    def base_url(self):
      return self.base_url

    def collections_url(self):
      return self.base_url + self.collections

    def conformance_url(self):
      return self.base_url + self.conformance

    def map_url(self):
      return self.base_url + self.map