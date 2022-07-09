from ogcmaps.utils.components import get_data
from ogcmaps.utils.urls import urls

landing_urls = urls().landing_urls()


def metadata(f="json") -> dict:
    """Retrieve the OGC API landing page for this service.

    Args:
        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: Links to the API definition, the conformance statements
        and to the feature collections in the dataset.

    Raises:
        None

    """

    data = get_data(landing_urls["landing_url"], f)
    return data
