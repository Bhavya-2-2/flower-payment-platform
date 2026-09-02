import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_create_payment(client):
    response = client.post(
        "/payments",
        json={
            "customer_id": "C1001",
            "amount": 500,
            "currency": "INR"
        }
    )

    assert response.status_code == 201
    assert response.json["status"] == "SUCCESS"


def test_invalid_amount(client):
    response = client.post(
        "/payments",
        json={
            "customer_id": "C1001",
            "amount": 0,
            "currency": "INR"
        }
    )

    assert response.status_code == 400


def test_missing_customer(client):
    response = client.post(
        "/payments",
        json={
            "amount": 500,
            "currency": "INR"
        }
    )

    assert response.status_code == 400


def test_get_payment(client):
    create_response = client.post(
        "/payments",
        json={
            "customer_id": "C1001",
            "amount": 500,
            "currency": "INR"
        }
    )

    payment_id = create_response.json["payment_id"]

    response = client.get(f"/payments/{payment_id}")

    assert response.status_code == 200
    assert response.json["payment_id"] == payment_id


def test_invalid_amount_type(client):
    response = client.post(
        "/payments",
        json={
            "customer_id": "C1001",
            "amount": "five hundred",
            "currency": "INR"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "amount must be a number"