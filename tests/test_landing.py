from pytest import fixture

from ogcmaps import landing


@fixture
def landing_keys():
    yield ["links"]


def test_landing(landing_keys):
    response = landing.metadata()

    assert isinstance(response, dict)
    assert set(landing_keys).issubset(
        response.keys()
    ), "All keys should be in the response"
