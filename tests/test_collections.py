from pathlib import Path

from pytest import fixture

from ogcmaps import collections


@fixture
def metadata_keys():
    yield ["links"]


def test_metadata(metadata_keys):
    response = collections.metadata()

    assert isinstance(response, dict)
    assert set(metadata_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_keys():
    yield [
        "links",
        "title",
        "extent",
        "crs",
        "storageCrs",
        "id",
        "dataType",
        "attribution",
        "minScaleDenominator",
        "minCellSize",
    ]


def test_get_collection(get_collection_keys):
    response = collections.get_collection("blueMarble")

    assert isinstance(response, dict)
    assert set(get_collection_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_map_keys():
    yield ["status", "fileName"]
    file_path = Path("map.png")
    file_path.unlink()


def test_get_collection_map(get_collection_map_keys):
    response = collections.get_collection_map("blueMarble", "map.png")

    assert isinstance(response, dict)
    assert set(get_collection_map_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_styles_keys():
    yield ["styles"]


def test_get_collection_styles(get_collection_styles_keys):
    response = collections.get_collection_styles("NaturalEarth")

    assert isinstance(response, dict)
    assert set(get_collection_styles_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_style_keys():
    yield ["version", "name", "sources", "sprite", "layers"]


def test_get_collection_style(get_collection_style_keys):
    response = collections.get_collection_style("NaturalEarth", "continents")

    assert isinstance(response, dict)
    assert set(get_collection_style_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_styled_map_keys():
    yield ["status", "fileName"]
    file_path = Path("map.png")
    file_path.unlink()


def test_get_collection_styled_map(get_collection_styled_map_keys):
    response = collections.get_collection_styled_map(
        "NaturalEarth", "continents", "map.png"
    )

    assert isinstance(response, dict)
    assert set(get_collection_styled_map_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_map_tiles_keys():
    yield ["links", "tilesets"]


def test_get_collection_map_tiles(get_collection_map_tiles_keys):
    response = collections.get_collection_map_tiles("NaturalEarth")

    assert isinstance(response, dict)
    assert set(get_collection_map_tiles_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@fixture
def get_collection_map_tile_matrix_keys():
    yield [
        "title",
        "tileMatrixSetURI",
        "crs",
        "dataType",
        "tileMatrixSetLimits",
        "links",
        "layers",
        "centerPoint",
    ]


def test_get_collection_map_tile_matrix(get_collection_map_tile_matrix_keys):
    response = collections.get_collection_map_tile_matrix(
        "NaturalEarth", "CDBGlobalGrid"
    )

    assert isinstance(response, dict)
    assert set(get_collection_map_tile_matrix_keys).issubset(
        response.keys()
    ), "All keys should be in the response"
