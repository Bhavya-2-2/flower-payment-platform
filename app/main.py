from flask import Flask
from app.routes import payment_routes

app = Flask(__name__)

app.register_blueprint(payment_routes)


@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "healthy",
        "service": "payment-api"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)