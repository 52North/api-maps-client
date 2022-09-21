# API Maps Client
Python client for OGC API - Maps.

## Installation
```bash
pip install ogcmaps
```

## Usage
```python
from ogcmaps import landing
data = landing.metadata()

print(data)
```

See the [docs](https://52north.github.io/api-maps-client/) for complete API documentation.

## For developers

Install
```bash
virtualenv env && source env/bin/activate
```
```bash
pip3 install -r requirements.txt
```
Install pre-commit and pytest
```bash
pip3 install pre-commit pytest
```
Build from source
```bash
pip3 install .
```

### Run tests
```bash
cd tests && pytest
```

### Generate docs
```bash
sphinx-apidoc -fo docs/source ogcmaps ogcmaps/utils/*
```
