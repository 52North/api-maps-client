import click

from ogcmaps import collections as collections_obj
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
    "--f",
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
    "--f",
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
