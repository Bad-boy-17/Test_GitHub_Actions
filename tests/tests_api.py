import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app
    app.testing = True
    return app.test_client()


def test_sub_api(client):
    response = client.get("/sub?a=5&b=3")

    assert response.status_code == 200
    assert response.get_json()["result"] == 2


def test_add_api(client):
    response = client.get("/add?a=2&b=3")

    assert response.status_code == 200
    assert response.get_json()["result"] == 5
