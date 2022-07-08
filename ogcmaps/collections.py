import requests

from ogcmaps.utils.components import uri, write
from ogcmaps.utils.urls import urls

collections_urls = urls().collections_urls()


def metadata(**kwargs) -> dict:
    """Retrieve the list of geospatial data collections available from this service.

    Args:
        datetime (str, optional): Either a date-time or an interval, half-bounded or
            bounded. Date and time expressions adhere to RFC 3339. Half-bounded
            intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../
              2018-03-18T12:31:12Z"

        bbox (array[int], optional): Only features that have a geometry that intersects
            the bounding box are selected. The bounding box is provided as four or six
            numbers,depending on whether the coordinate reference system includes a
            vertical axis (height or depth):

            * Lower left corner, coordinate axis 1
            * Lower left corner, coordinate axis 2
            * Minimum value, coordinate axis 3 (optional)
            * Upper right corner, coordinate axis 1
            * Upper right corner, coordinate axis 2
            * Maximum value, coordinate axis 3 (optional)

            The coordinate reference system of the values is WGS 84 longitude/
            latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a
            different coordinate reference system is specified in the parameter
            ``bbox-crs``. For WGS 84 longitude/latitude the values are in most cases
            the sequence of minimum longitude, minimum latitude, maximum longitude and
            maximum latitude. However, in cases where the box spans the antimeridian
            the first value (west-most box edge) is larger than the third value
            (east-most box edge). If the vertical axis is included, the third and the
            sixth number are the bottom and the top of the 3-dimensional bounding box.
            If a feature has multiple spatial geometry properties, it is the decision
            of the server whether only a single spatial geometry property is used to
            determine the extent or all relevant geometries.


        limit (int, optional): The optional limit parameter limits the number of
            collections that are presented in the response document. Only items are
            counted that are on the first level of the collection in the response
            document. Nested objects contained within the explicitly requested items
            shall not be counted.

            * Minimum = 1 * Maximum = 10000 * Default = 10

            `Default value : 10`

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: The collections of (mostly geospatial) data available from this API.
        The dataset contains one or more collections. This resource provides
        information about and access to the collections. The response contains the
        list of collections. Each collection is accessible via one or more OGC API
        set of specifications, for which a link to relevant accessible resources,
        e.g. ``/collections/{collectionId}/(items, coverage, map, tiles...)`` is
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
        ValueError: If parameter is invalid

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

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: Information about a particular collection of (mostly geospatial) data
        available from this API. The collection is accessible via one or more OGC
        API set of specifications, for which a link to relevant accessible
        resources, e.g. ``/collections/{collectionId}/(items, coverage, map, tiles...)``
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
        None
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
    """Retrieve a map for the specified collection.

    Args:
        collection_id (str): Local identifier of a collection

        file_name (str): Name of file to save the map image

        bbox (array[int], optional): Only features that have a geometry that intersects
            the bounding box are selected. The bounding box is provided as four or six
            numbers, depending on whether the coordinate reference system includes a
            vertical axis (height or depth):

            * Lower left corner, coordinate axis 1
            * Lower left corner, coordinate axis 2
            * Minimum value, coordinate axis 3 (optional)
            * Upper right corner, coordinate axis 1
            * Upper right corner, coordinate axis 2
            * Maximum value, coordinate axis 3 (optional)

            The coordinate reference system of the values is WGS 84 longitude/latitude
            (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
            reference system is specified in the parameter bbox-crs. For WGS 84
            longitude/latitude the values are in most cases the sequence of minimum
            longitude, minimum latitude, maximum longitude and maximum latitude.
            However, in cases where the box spans the antimeridian the first value
            (west-most box edge) is larger than the third value (east-most box edge). If
            the vertical axis is included, the third and the sixth number are the bottom
            and the top of the 3-dimensional bounding box. If a feature has multiple
            spatial geometry properties, it is the decision of the server whether only a
            single spatial geometry property is used to determine the extent or all
            relevant geometries.

        datetime (str, optional):Either a date-time or an interval, half-bounded or
            bounded. Date and time expressions adhere to RFC 3339. Half-bounded
            intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../
              2018-03-18T12:31:12Z"

        collections (array[str], optional): The collections that should be included in
            the response. The parameter value is a comma-separated list of collection
            identifiers. If the parameters is missing, some or all collections will be
            included. The collection will be rendered in the order specified, with the
            last one showing on top, unless the priority is overridden by styling rules.

        subset (array[str], optional): Retrieve only part of the data by slicing or
            trimming along one or more axis For trimming: ``{axisAbbrev}({low}:{high})``
            (preserves dimensionality) An asterisk ``(*)`` can be used instead of
            ``{low}`` or ``{high}`` to indicate the minimum/maximum value. For
            slicing: ``{axisAbbrev}({value})`` (reduces dimensionality).

        crs (str, optional): Reproject the output to the given crs

        bbox-crs (str, optional): Crs for the specified bbox

        subset-crs (str, optional): Crs for the specified subset

        bgcolor (str, optional): Web color name or hexadecimal `0x[AA]RRGGBB` color
            value for the background color (default to `0x9C9C9C` gray). If alpha is not
            specified, full opacity is assumed.

            `Default value : 0xFFFFFF`

        transparent (boolean, optional): Background transparency of map (default=true).

            `Default value : true`

        width (int, optional): Width of the map in pixel. If omitted and height is
            specified, defaults to the width maintaining a 1:1 aspect ratio. If both
            width and height are omitted, the server will select a default dimensions.

        height (int, optional): Height of the map in pixel. If omitted and width is
            specified, defaults to the height maintaining a 1:1 aspect ratio. If both
            width and height are omitted, the server will select a default dimensions.

        f (str, optional): The format of the map response (e.g. png). Accepted values
            are 'png', 'jpg' or 'tiff' (GeoTIFF).

            `Available values : png, jpg, tiff`

    Returns:
        JSON: Status message and file name

    Raises:
        ValueError: If parameter is invalid

    """

    keys = [
        "crs",
        "bbox",
        "bbox-crs",
        "width",
        "height",
        "transparent",
        "bgcolor",
        "collections",
        "datetime",
        "subset",
        "subset-crs",
        "f",
    ]

    get_collection_map_url = collections_urls["get_collection_map"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
    )
    endpoint = uri(get_collection_map_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write(endpoint, file_name)
        return write_file

    return endpoint


def get_collection_styles(collection_id) -> dict:
    """Retrieve the list of all styles for a particular collection.

    Args:
        collection_id (str): Local identifier of a collection

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: A list of styles and the style data

    Raises:
        None
    """

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
    """Retrieve the style data for a style in a collection.

    Args:
        collection_id (str): Local identifier of a collection

        style_id (str): An identifier representing a specific style.

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: Style data of a particular style

    Raises:
        None
    """

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


def get_collection_styled_map(collection_id, style_id, file_name, **kwargs) -> dict:
    """Retrieve a map for a specified collection and style.

    Args:
        collection_id (str): Local identifier of a collection

        style_id (str): An identifier representing a specific style

        file_name (str): Name of file to save the map image

        bbox (array[int], optional): Only features that have a geometry that intersects
            the bounding box are selected. The bounding box is provided as four or six
            numbers, depending on whether the coordinate reference system includes a
            vertical axis (height or depth):

            * Lower left corner, coordinate axis 1
            * Lower left corner, coordinate axis 2
            * Minimum value, coordinate axis 3 (optional)
            * Upper right corner, coordinate axis 1
            * Upper right corner, coordinate axis 2
            * Maximum value, coordinate axis 3 (optional)

            The coordinate reference system of the values is WGS 84 longitude/latitude
            (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
            reference system is specified in the parameter bbox-crs. For WGS 84
            longitude/latitude the values are in most cases the sequence of minimum
            longitude, minimum latitude, maximum longitude and maximum latitude.
            However, in cases where the box spans the antimeridian the first value
            (west-most box edge) is larger than the third value (east-most box edge). If
            the vertical axis is included, the third and the sixth number are the bottom
            and the top of the 3-dimensional bounding box. If a feature has multiple
            spatial geometry properties, it is the decision of the server whether only a
            single spatial geometry property is used to determine the extent or all
            relevant geometries.

        datetime (str, optional):Either a date-time or an interval, half-bounded or
            bounded. Date and time expressions adhere to RFC 3339. Half-bounded
            intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../
              2018-03-18T12:31:12Z"

        collections (array[str], optional): The collections that should be included in
            the response. The parameter value is a comma-separated list of collection
            identifiers. If the parameters is missing, some or all collections will be
            included. The collection will be rendered in the order specified, with the
            last one showing on top, unless the priority is overridden by styling rules.

        subset (array[str], optional): Retrieve only part of the data by slicing or
            trimming along one or more axis For trimming: ``{axisAbbrev}({low}:{high})``
            (preserves dimensionality) An asterisk ``(*)`` can be used instead of
            ``{low}`` or ``{high}`` to indicate the minimum/maximum value. For
            slicing: ``{axisAbbrev}({value})`` (reduces dimensionality).

        crs (str, optional): Reproject the output to the given crs

        bbox-crs (str, optional): Crs for the specified bbox

        subset-crs (str, optional): Crs for the specified subset

        bgcolor (str, optional): Web color name or hexadecimal `0x[AA]RRGGBB` color
            value for the background color (default to `0x9C9C9C` gray). If alpha is not
            specified, full opacity is assumed.

            `Default value : 0xFFFFFF`

        transparent (boolean, optional): Background transparency of map (default=true).

            `Default value : true`

        width (int, optional): Width of the map in pixel. If omitted and height is
            specified, defaults to the width maintaining a 1:1 aspect ratio. If both
            width and height are omitted, the server will select a default dimensions.

        height (int, optional): Height of the map in pixel. If omitted and width is
            specified, defaults to the height maintaining a 1:1 aspect ratio. If both
            width and height are omitted, the server will select a default dimensions.

        f (str, optional): The format of the map response (e.g. png). Accepted values
            are 'png', 'jpg' or 'tiff' (GeoTIFF).

            `Available values : png, jpg, tiff`

    Returns:
        JSON: Status message and file name

    Raises:
        ValueError: If parameter is invalid
    """

    keys = [
        "crs",
        "bbox",
        "bbox-crs",
        "width",
        "height",
        "transparent",
        "bgcolor",
        "collections",
        "datetime",
        "subset",
        "subset-crs",
        "f",
    ]

    get_styled_map_url = collections_urls["get_collection_styled_map"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        style_id=style_id,
    )
    endpoint = uri(get_styled_map_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write(endpoint, file_name)
        return write_file

    return endpoint


def get_collection_map_tiles(collection_id) -> dict:
    """Retrieve a list of all map tilesets for specified collection.

    Args:
        collection_id (str): Local identifier of a collection

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: List of available tilesets.

    Raises:
        None
    """

    get_map_tiles_url = collections_urls["get_collection_map_tiles"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
    )
    collection_map_tiles = requests.get(
        get_map_tiles_url, headers=urls().json_headers
    ).json()
    return collection_map_tiles


def get_collection_map_tile_matrix(collection_id, tile_matrix_set_id) -> dict:
    """Retrieve a map tile set metadata for the specified collection and tiling scheme
    (tile matrix set)

    Args:
        collection_id (str): Local identifier of a collection

        tile_matrix_set_id (str): Identifier for a supported TileMatrixSet

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: Description of the tileset.

    Raises:
        None
    """

    get_map_tile_matrix_url = collections_urls["get_collection_map_tile_matrix"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        tile_matrix_set_id=tile_matrix_set_id,
    )
    map_tile_matrix = requests.get(
        get_map_tile_matrix_url, headers=urls().json_headers
    ).json()
    return map_tile_matrix


def get_collection_map_tile(
    collection_id,
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    **kwargs,
) -> dict:
    """Retrieve a map tile from the specified collection.

    Args:
        collection_id (str): Local identifier of a collection

        tile_matrix_set_id (str): Identifier for a supported TileMatrixSet

        tile_matrix (str): Identifier selecting one of the scales defined in the
            TileMatrixSet and representing the scaleDenominator the tile. For example,
            Ireland is fully within the Tile at WebMercatorQuad ``tileMatrix=5``,
            ``tileRow=10`` and ``tileCol=15``.

            `Example : 5`

        tile_row (int): Row index of the tile on the selected TileMatrix. It cannot
            exceed the MatrixWidth-1 for the selected TileMatrix. For example, Ireland
            is fully within the Tile at WebMercatorQuad ``tileMatrix=5``,
            ``tileRow=10`` and ``tileCol=15``.

            `Example : 10`

        tile_col (int): Column index of the tile on the selected TileMatrix. It cannot
            exceed the MatrixHeight-1 for the selected TileMatrix. For example, Ireland
            is fully within the Tile at WebMercatorQuad ``tileMatrix=5``, ``tileRow=10``
            and ``tileCol=15``.

            `Example : 15`

        file_name (str): Name of file to save the map image

        datetime (str, optional):Either a date-time or an interval, half-bounded or
            bounded. Date and time expressions adhere to RFC 3339. Half-bounded
            intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../
              2018-03-18T12:31:12Z"

        collections (array[str], optional): The collections that should be included in
            the response. The parameter value is a comma-separated list of collection
            identifiers. If the parameters is missing, some or all collections will be
            included. The collection will be rendered in the order specified, with the
            last one showing on top, unless the priority is overridden by styling rules.

        subset (array[str], optional): Retrieve only part of the data by slicing or
            trimming along one or more axis For trimming: ``{axisAbbrev}({low}:{high})``
            (preserves dimensionality) An asterisk ``(*)`` can be used instead of
            ``{low}`` or ``{high}`` to indicate the minimum/maximum value. For
            slicing: ``{axisAbbrev}({value})`` (reduces dimensionality).

        crs (str, optional): Reproject the output to the given crs

        subset-crs (str, optional): Crs for the specified subset

        bgcolor (str, optional): Web color name or hexadecimal `0x[AA]RRGGBB` color
            value for the background color (default to `0x9C9C9C` gray). If alpha is not
            specified, full opacity is assumed.

            `Default value : 0xFFFFFF`

        transparent (boolean, optional): Background transparency of map (default=true).

            `Default value : true`

        f (str, optional): The format of the map response (e.g. png). Accepted values
            are 'png', 'jpg' or 'tiff' (GeoTIFF).

            `Available values : png, jpg, tiff`

    Returns:
        JSON: Status message and file name

    Raises:
        ValueError: If parameter is invalid
    """

    keys = [
        "crs",
        "transparent",
        "bgcolor",
        "collections",
        "datetime",
        "subset",
        "subset-crs",
        "f",
    ]

    get_collection_map_tile = collections_urls["get_collection_map_tile"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        tile_matrix_set_id=tile_matrix_set_id,
        tile_matrix=tile_matrix,
        tile_row=tile_row,
        tile_col=tile_col,
    )
    endpoint = uri(get_collection_map_tile, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write(endpoint, file_name)
        return write_file

    return endpoint


def get_collection_styled_tiles(collection_id, style_id) -> dict:
    """Retrieve a list of styled map tilesets for the specified collection

    Args:
        collection_id (str): Local identifier of a collection

        style_id (str): An identifier representing a specific style

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: List of available tilesets

    Raises:
        None
    """

    get_styled_tiles_url = collections_urls["get_collection_styled_tiles"].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        style_id=style_id,
    )
    styled_tiles = requests.get(
        get_styled_tiles_url, headers=urls().json_headers
    ).json()
    return styled_tiles


def collection_styled_map_tile_matrix(
    collection_id, style_id, tile_matrix_set_id, **kwargs
) -> dict:
    """Retrieve the map tileset metadata for the specified collection, style and tiling
    scheme (tile matrix set).

    Args:
        collection_id (str): Local identifier of a collection

        style_id (str): An identifier representing a specific style

        tile_matrix_set_id (str): Identifier for a supported TileMatrixSet

        collections (array[str], optional): The collections that should be included in
            the response. The parameter value is a comma-separated list of collection
            identifiers. If the parameters is missing, some or all collections will be
            included. The collection will be rendered in the order specified, with the
            last one showing on top, unless the priority is overridden by styling rules.

        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: Description of the tileset

    Raises:
        None
    """

    keys = ["collections", "f"]

    styled_map_tile_matrix_url = collections_urls[
        "collection_styled_map_tile_matrix"
    ].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        tile_matrix_set_id=tile_matrix_set_id,
        style_id=style_id,
    )
    endpoint = uri(styled_map_tile_matrix_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        get_styled_map_tile_matrix = requests.get(
            endpoint["endpoint"], headers=urls().json_headers
        ).json()
        return get_styled_map_tile_matrix

    return endpoint


def get_collection_styled_map_tile(
    collection_id,
    style_id,
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    **kwargs,
) -> dict:
    """Retrieve a map tile for a specified collection and style

    Args:
        collection_id (str): Local identifier of a collection

        style_id (str): An identifier representing a specific style

        tile_matrix_set_id (str): Identifier for a supported TileMatrixSet

        tile_matrix (str): Identifier selecting one of the scales defined in the
            TileMatrixSet and representing the scaleDenominator the tile. For example,
            Ireland is fully within the Tile at WebMercatorQuad ``tileMatrix=5``,
            ``tileRow=10`` and ``tileCol=15``.

            `Example : 5`

        tile_row (int): Row index of the tile on the selected TileMatrix. It cannot
            exceed the MatrixWidth-1 for the selected TileMatrix. For example, Ireland
            is fully within the Tile at WebMercatorQuad ``tileMatrix=5``,
            ``tileRow=10`` and ``tileCol=15``.

            `Example : 10`

        tile_col (int): Column index of the tile on the selected TileMatrix. It cannot
            exceed the MatrixHeight-1 for the selected TileMatrix. For example, Ireland
            is fully within the Tile at WebMercatorQuad ``tileMatrix=5``, ``tileRow=10``
            and ``tileCol=15``.

            `Example : 15`

        file_name (str): Name of file to save the map image

        datetime (str, optional):Either a date-time or an interval, half-bounded or
            bounded. Date and time expressions adhere to RFC 3339. Half-bounded
            intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../
              2018-03-18T12:31:12Z"

        collections (array[str], optional): The collections that should be included in
            the response. The parameter value is a comma-separated list of collection
            identifiers. If the parameters is missing, some or all collections will be
            included. The collection will be rendered in the order specified, with the
            last one showing on top, unless the priority is overridden by styling rules.

        subset (array[str], optional): Retrieve only part of the data by slicing or
            trimming along one or more axis For trimming: ``{axisAbbrev}({low}:{high})``
            (preserves dimensionality) An asterisk ``(*)`` can be used instead of
            ``{low}`` or ``{high}`` to indicate the minimum/maximum value. For
            slicing: ``{axisAbbrev}({value})`` (reduces dimensionality).

        crs (str, optional): Reproject the output to the given crs

        subset-crs (str, optional): Crs for the specified subset

        bgcolor (str, optional): Web color name or hexadecimal `0x[AA]RRGGBB` color
            value for the background color (default to `0x9C9C9C` gray). If alpha is not
            specified, full opacity is assumed.

            `Default value : 0xFFFFFF`

        transparent (boolean, optional): Background transparency of map (default=true).

            `Default value : true`

        f (str, optional): The format of the map response (e.g. png). Accepted values
            are 'png', 'jpg' or 'tiff' (GeoTIFF).

            `Available values : png, jpg, tiff`

    Returns:
        JSON: Status message and file name

    Raises:
        ValueError: If parameter is invalid

    """

    keys = [
        "crs",
        "transparent",
        "bgcolor",
        "collections",
        "datetime",
        "subset",
        "subset-crs",
        "f",
    ]

    get_collection_styled_map_tile = collections_urls[
        "collection_styled_map_tile"
    ].format(
        base_url=urls().base_url,
        collections=urls().collections,
        collection_id=collection_id,
        style_id=style_id,
        tile_matrix_set_id=tile_matrix_set_id,
        tile_matrix=tile_matrix,
        tile_row=tile_row,
        tile_col=tile_col,
    )
    endpoint = uri(get_collection_styled_map_tile, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write(endpoint, file_name)
        return write_file

    return endpoint
