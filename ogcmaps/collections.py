import requests

from ogcmaps.utils.components import uri
from ogcmaps.utils.urls import urls

collections_urls = urls().collections_urls()


def metadata(**kwargs) -> dict:
    """Retrieve the list of geospatial data collections available from this service.

    Args:
        None

    Returns:
        JSON: The collections of (mostly geospatial) data available from this API.
        The dataset contains one or more collections. This resource provides
        information about and access to the collections. The response contains the
        list of collections. Each collection is accessible via one or more OGC API
        set of specifications, for which a link to relevant accessible resources,
        e.g. `/collections/{collectionId}/(items, coverage, map, tiles...)` is
        provided, with the corresponding relation type, as well as key information
        about the collection. This information includes:

        * A local identifier for the collection that is unique for the dataset.
        * A list of coordinate reference systems (CRS) in which data may be returned by
        the server. The first CRS is the default coordinate reference system (the
        default is always WGS 84 with axis order longitude/latitude).
        * An optional title and description for the collection.
        * An optional extent that can be used to provide an indication of the spatial
        and temporal extent of the collection - typically derived from the data.
        * For collections accessible via the Features or Records API, an optional
        indicator about the type of the items in the collection (the default value, if
        the indicator is not provided, is 'feature').


    Raises:
        None

    """

    keys = ["datetime", "bbox", "limit", "f"]

    get_collection_url = collections_urls["collections_url"]
    endpoint = uri(get_collection_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        get_collections = requests.get(
            endpoint["endpoint"], headers=urls().json_headers
        ).json()
        return get_collections

    return endpoint


def get_collection(collection_id) -> dict:
    """Retrieve the description of a collection available from this service.

    Args:
        collection_id (str): Local identifier of a collection

    Returns:
        Information about a particular collection of (mostly geospatial) data
        available from this API. The collection is accessible via one or more OGC
        API set of specifications, for which a link to relevant accessible
        resources, e.g. /collections/{collectionId}/(items, coverage, map, tiles...)
        is contained in the response, with the corresponding relation type, as well
        as key information about the collection. This information includes:

        * A local identifier for the collection that is unique for the dataset.
        * A list of coordinate reference systems (CRS) in which data may be returned
        by the server. The first CRS is the default coordinate reference system (the
        default is always WGS 84 with axis order longitude/latitude).
        * An optional title and description for the collection.
        * An optional extent that can be used to provide an indication of the
        spatial and temporal extent of the collection - typically derived from the
        data.
        * For collections accessible via the Features or Records API, an optional
        indicator about the type of the items in the collection (the default value, if
        the indicator is not provided, is 'feature').


    Raises:
        ValueError: If parameter is invalid
    """

    get_collection_url = collections_urls["get_collection"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
    )
    get_collection_data = requests.get(
        get_collection_url, headers=urls().json_headers
    ).json()
    return get_collection_data


def get_collection_map(collection_id, file_name, **kwargs) -> dict:

    keys = [
        "crs",
        "bbox",
        "width",
        "height",
        "cell-size",
        "transparent",
        "bgcolor",
        "datetime",
        "elevation",
        "f",
    ]

    get_collection_map_url = collections_urls["get_collection_map"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
    )
    endpoint = uri(get_collection_map_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        map_data = requests.get(endpoint["endpoint"])
        file = open(f"{file_name}", "wb")
        file.write(map_data.content)
        file.close()
        return {"status": "success", "file name": f"{file_name}"}

    return endpoint


def get_collection_styles(collection_id) -> dict:

    get_collection_styles_url = collections_urls["get_collection_styles"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
    )
    collection_styles = requests.get(
        get_collection_styles_url, headers=urls().json_headers
    ).json()
    return collection_styles


def get_collection_style(collection_id, style_id) -> dict:

    get_collection_style_url = collections_urls["get_collection_style"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        style_id=style_id,
    )
    collection_style = requests.get(
        get_collection_style_url, headers=urls().json_headers
    ).json()
    return collection_style
