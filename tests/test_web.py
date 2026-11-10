"""Интеграционные проверки HTTP-маршрутов Flask."""
from studyshop.web import create_app


def test_health():
    client = create_app().test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_calculate_success():
    client = create_app().test_client()
    response = client.get("/calculate?price=100&quantity=3&discount=10")
    assert response.status_code == 200
    assert response.get_json()["total"] == 270


def test_calculate_validation():
    client = create_app().test_client()
    response = client.get("/calculate?price=-1&quantity=3")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_calculate_missing_parameter():
    client = create_app().test_client()
    response = client.get("/calculate?quantity=3")
    assert response.status_code == 400
