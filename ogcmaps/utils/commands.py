import click

from ogcmaps import collections as collections_obj
from ogcmaps import conformance as conformance_obj
from ogcmaps import landing as landing_obj
from ogcmaps import maps as maps_obj
from ogcmaps import styles as styles_obj
from ogcmaps.utils.components import parse_options, printer


@click.command(
    "collections_metadata",
    short_help=(
        "Retrieve the list of geospatial data "
        "collections available from this service."
    ),
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def collections_metadata(ctx, f):

    click.echo(printer(ctx, collections_obj.metadata(f=f)))


@click.command(
    "collection_styled_map_tile_matrix",
    short_help=(
        "Retrieve the map tileset metadata for the specified "
        "collection, style and tiling scheme (tile matrix set)."
    ),
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help="Identifier for a supported TileMatrixSet.",
)
@click.option(
    "--collections",
    default="",
    help="The collections that should be included in the response.",
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def collection_styled_map_tile_matrix(
    ctx, collection_id, style_id, tile_matrix_set_id, collections, f
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            collections_obj.collection_styled_map_tile_matrix(
                collection_id=collection_id,
                style_id=style_id,
                tile_matrix_set_id=tile_matrix_set_id,
                collections=collections,
                f=f,
                **options
            ),
        )
    )


@click.command(
    "get_collection",
    short_help="Retrieve the description of a collection available from this service.",
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection(ctx, collection_id, f):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection(
                collection_id=collection_id,
                f=f,
            ),
        )
    )


@click.command(
    "get_collection_map",
    short_help="Retrieve a map for the specified collection.",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_collection_map(ctx, collection_id, file_name, f):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_map(
                collection_id=collection_id, file_name=file_name, f=f, **options
            ),
        )
    )


@click.command(
    "get_collection_map_tile",
    short_help="Retrieve a map tile from the specified collection.",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help=("Identifier for a supported" "TileMatrixSet"),
)
@click.option(
    "--tile_matrix",
    required=True,
    help=("Identifier selecting one of the scales" "defined in the TileMatrixSet"),
)
@click.option(
    "--tile_row",
    required=True,
    help=("Row index of the tile on the " "selected TileMatrix."),
)
@click.option(
    "--tile_col",
    required=True,
    help=("Column index of the tile on the " "selected TileMatrix."),
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_collection_map_tile(
    ctx,
    collection_id,
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_map_tile(
                collection_id=collection_id,
                tile_matrix_set_id=tile_matrix_set_id,
                tile_matrix=tile_matrix,
                tile_row=tile_row,
                tile_col=tile_col,
                file_name=file_name,
                f=f,
                **options
            ),
        )
    )


@click.command(
    "get_collection_map_tile_matrix",
    short_help=(
        "Retrieve a map tile set metadata for the specified "
        "collection and tiling scheme (tile matrix set)."
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help=("Identifier for a supported" "TileMatrixSet"),
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection_map_tile_matrix(
    ctx,
    collection_id,
    tile_matrix_set_id,
    f,
):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_map_tile_matrix(
                collection_id=collection_id, tile_matrix_set_id=tile_matrix_set_id, f=f
            ),
        )
    )


@click.command(
    "get_collection_map_tiles",
    short_help="Retrieve a list of all map tilesets for specified collection.",
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection_map_tiles(
    ctx,
    collection_id,
    f,
):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_map_tiles(collection_id=collection_id, f=f),
        )
    )


@click.command(
    "get_collection_style",
    short_help="Retrieve the style data for a style in a collection.",
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection_style(
    ctx,
    collection_id,
    style_id,
    f,
):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_style(
                collection_id=collection_id, style_id=style_id, f=f
            ),
        )
    )


@click.command(
    "get_collection_styled_map",
    short_help="Retrieve a map for a specified collection and style.",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_collection_styled_map(
    ctx,
    collection_id,
    style_id,
    file_name,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_styled_map(
                collection_id=collection_id,
                style_id=style_id,
                file_name=file_name,
                f=f,
                **options
            ),
        )
    )


@click.command(
    "get_collection_styled_map_tile",
    short_help="Retrieve a map tile for a specified collection and style",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help=("Identifier for a supported" "TileMatrixSet"),
)
@click.option(
    "--tile_matrix",
    required=True,
    help=("Identifier selecting one of the scales" "defined in the TileMatrixSet"),
)
@click.option(
    "--tile_row",
    required=True,
    help=("Row index of the tile on the " "selected TileMatrix."),
)
@click.option(
    "--tile_col",
    required=True,
    help=("Column index of the tile on the " "selected TileMatrix."),
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_collection_styled_map_tile(
    ctx,
    collection_id,
    style_id,
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_styled_map_tile(
                collection_id=collection_id,
                style_id=style_id,
                tile_matrix_set_id=tile_matrix_set_id,
                tile_matrix=tile_matrix,
                tile_row=tile_row,
                tile_col=tile_col,
                file_name=file_name,
                f=f,
                **options
            ),
        )
    )


@click.command(
    "get_collection_styled_tiles",
    short_help="Retrieve a list of styled map tilesets for the specified collection",
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection_styled_tiles(
    ctx,
    collection_id,
    style_id,
    f,
):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_styled_tiles(
                collection_id=collection_id,
                style_id=style_id,
                f=f,
            ),
        )
    )


@click.command(
    "get_collection_styles",
    short_help="Retrieve the list of all styles for a particular collection.",
)
@click.option(
    "--collection_id", required=True, help="Local identifier of a collection."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_collection_styles(
    ctx,
    collection_id,
    f,
):

    click.echo(
        printer(
            ctx,
            collections_obj.get_collection_styles(
                collection_id=collection_id,
                f=f,
            ),
        )
    )


@click.command(
    "conformance_metadata",
    short_help=(
        "Retrieve the set of OGC API conformance classes that "
        "are supported by this service."
    ),
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def conformance_metadata(
    ctx,
    f,
):

    click.echo(
        printer(
            ctx,
            conformance_obj.metadata(
                f=f,
            ),
        )
    )


@click.command(
    "landing_metadata",
    short_help="Retrieve the OGC API landing page for this service.",
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def landing_metadata(
    ctx,
    f,
):

    click.echo(
        printer(
            ctx,
            landing_obj.metadata(
                f=f,
            ),
        )
    )


@click.command(
    "get_styled_map",
    short_help="Retrieve a styled map of the whole dataset.",
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_styled_map(
    ctx,
    style_id,
    file_name,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            styles_obj.get_styled_map(
                style_id=style_id, file_name=file_name, f=f, **options
            ),
        )
    )


@click.command(
    "get_styled_map_tile",
    short_help="Retrieve a styled map tile.",
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help=("Identifier for a supported" "TileMatrixSet"),
)
@click.option(
    "--tile_matrix",
    required=True,
    help=("Identifier selecting one of the scales" "defined in the TileMatrixSet"),
)
@click.option(
    "--tile_row",
    required=True,
    help=("Row index of the tile on the " "selected TileMatrix."),
)
@click.option(
    "--tile_col",
    required=True,
    help=("Column index of the tile on the " "selected TileMatrix."),
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_styled_map_tile(
    ctx,
    style_id,
    tile_matrix_set_id,
    tile_matrix,
    tile_row,
    tile_col,
    file_name,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            styles_obj.get_styled_map_tile(
                style_id=style_id,
                tile_matrix_set_id=tile_matrix_set_id,
                tile_matrix=tile_matrix,
                tile_row=tile_row,
                tile_col=tile_col,
                file_name=file_name,
                f=f,
                **options
            ),
        )
    )


@click.command(
    "get_styled_map_tiles",
    short_help="Retrieve the list of styled map tilesets for the whole dataset.",
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def get_styled_map_tiles(
    ctx,
    style_id,
    f,
):

    click.echo(
        printer(
            ctx,
            styles_obj.get_styled_map_tiles(
                style_id=style_id,
                f=f,
            ),
        )
    )


@click.command(
    "styled_map_tiles_matrix",
    short_help=(
        "Retrieve a styled map tileset of the whole dataset "
        "for the specified tiling scheme (tile matrix set)"
    ),
)
@click.option(
    "--style_id", required=True, help="An identifier representing a specific style."
)
@click.option(
    "--tile_matrix_set_id",
    required=True,
    help=("Identifier for a supported" "TileMatrixSet"),
)
@click.option(
    "-f",
    default="json",
    help="The format of the response. Accepted values are 'json' or 'html'.",
)
@click.pass_context
def styled_map_tiles_matrix(
    ctx,
    style_id,
    tile_matrix_set_id,
    f,
):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            styles_obj.styled_map_tiles_matrix(
                style_id=style_id, tile_matrix_set_id=tile_matrix_set_id, f=f, **options
            ),
        )
    )


@click.command(
    "get_map",
    short_help="Retrieve a default map of the whole dataset.",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.option("--file_name", required=True, help="Name of file to save the map image.")
@click.option(
    "-f",
    default="png",
    help=(
        "The format of the map response (e.g. png). Accepted values "
        "are 'png', 'jpg' or 'tiff' (GeoTIFF)."
    ),
)
@click.pass_context
def get_map(ctx, file_name, f):

    options = parse_options(ctx)
    click.echo(
        printer(
            ctx,
            maps_obj.get_map(file_name=file_name, f=f, **options),
        )
    )
