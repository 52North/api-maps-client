from pytest import fixture

from ogcmaps import conformance


@fixture
def conformance_keys():
    yield ["type", "links", "conformsTo", "properties"]


def test_conformance(conformance_keys):
    response = conformance.metadata()

    assert isinstance(response, dict)
    assert set(conformance_keys).issubset(
        response.keys()
    ), "All keys should be in the response"
