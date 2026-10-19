from flask import Blueprint, request
import uuid

payment_routes = Blueprint("payment_routes", __name__)

payments = {}


@payment_routes.route("/payments", methods=["POST"])
def create_payment():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    customer_id = data.get("customer_id")
    amount = data.get("amount")
    currency = data.get("currency")

    if not isinstance(customer_id, str) or not customer_id.strip():
        return {"error": "customer_id must be a non-empty string"}, 400

    customer_id = customer_id.strip()

    if not isinstance(amount, (int, float)):
        return {"error": "amount must be a number"}, 400

    if amount <= 0:
        return {"error": "amount must be greater than zero"}, 400

    if currency not in ["INR", "USD"]:
        return {"error": "Unsupported currency"}, 400

    payment_id = str(uuid.uuid4())

    payment = {
        "payment_id": payment_id,
        "customer_id": customer_id,
        "amount": amount,
        "currency": currency,
        "status": "SUCCESS"
    }

    payments[payment_id] = payment

    return payment, 201


@payment_routes.route("/payments/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    payment = payments.get(payment_id)

    if not payment:
        return {"error": "Payment not found"}, 404

    return payment, 200
