import requests

from ogcmaps.utils.urls import urls

landing_urls = urls().landing_urls()


def metadata() -> dict:
    """Retrieve the OGC API landing page for this service.

    Args:
        None

    Returns:
        JSON: Links to the API definition, the conformance statements
        and to the feature collections in the dataset.

    Raises:
        None

    """

    landing_data = requests.get(
        landing_urls["landing_url"], headers=urls().json_headers
    ).json()
    return landing_data
