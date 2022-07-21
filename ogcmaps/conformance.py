from ogcmaps.utils.components import get_data
from ogcmaps.utils.urls import urls

conformance_urls = urls().conformance_urls()


def metadata(f="json") -> dict:
    """Retrieve the set of OGC API conformance classes that are supported by this
    service.

    Args:
        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: The URIs of all conformance classes supported by the server

    Raises:
        None

    """

    data = get_data(conformance_urls["conformance_url"], f)
    return data
