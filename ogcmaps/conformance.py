import requests

from ogcmaps.utils.urls import urls

conformance_urls = urls().conformance_urls()


def metadata() -> dict:

    conformance_data = requests.get(
        conformance_urls["conformance_url"],
        headers=urls().json_headers,
    ).json()
    return conformance_data
