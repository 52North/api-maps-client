from ogcmaps.utils.components import get_data, uri, write_image
from ogcmaps.utils.urls import urls

map_urls = urls().map_urls()


def get_map(file_name, f="png", **kwargs) -> dict:
    """Retrieve a default map of the whole dataset

    Args:
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
        JSON: Status message and File name

    Raises:
        None
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

    endpoint = uri(map_urls["map_url"], keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write_image(endpoint, file_name, f)
        return write_file

    return endpoint


def get_map_tiles(f="json") -> dict:
    """Retrieve the list of all default map tilesets for the whole dataset

    Args:
        f (str, optional): The format of the response. If no value is provided, the
            accept header is used to determine the format. Accepted values are 'json' or
            'html'.

            `Available values : json, html`

    Returns:
        JSON: List of available tilesets

    Raises:
        None
    """

    data = get_data(map_urls["get_map_tiles"], f)
    return data


def get_map_tile_matrix_set(tile_matrix_set_id, f="json", **kwargs) -> dict:
    """Retrieve a default map tileset of the whole dataset for the specified tiling
    scheme (tile matrix set)

    Args:
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
        ValueError: If parameter is invalid
    """

    keys = ["collections", "f"]

    map_tile_matrix_url = map_urls["map_tile_matrix_set"].format(
        base_url=urls().base_url,
        map=urls().map,
        tile_matrix_set_id=tile_matrix_set_id,
    )

    endpoint = uri(map_tile_matrix_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        data = get_data(endpoint["endpoint"], f)
        return data

    return endpoint


def get_map_tile(
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    f="png",
    **kwargs,
) -> dict:
    """Retrieve a default map tile of the whole dataset

    Args:
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

    get_map_tile_url = map_urls["get_map_tile"].format(
        base_url=urls().base_url,
        map=urls().map,
        tile_matrix_set_id=tile_matrix_set_id,
        tile_matrix=tile_matrix,
        tile_row=tile_row,
        tile_col=tile_col,
    )
    endpoint = uri(get_map_tile_url, keys, **kwargs)
    if next(iter(endpoint)) == "endpoint":
        write_file = write_image(endpoint, file_name, f)
        return write_file

    return endpoint
