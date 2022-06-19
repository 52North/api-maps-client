import json

def jsonify(data):
  raw_data = json.load(data)
  return json.dumps(raw_data, indent=2)