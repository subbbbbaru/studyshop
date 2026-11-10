"""Веб-интерфейс существующей логики StudyShop на Flask."""
from flask import Flask, jsonify, request
from .pricing import total_cost


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify({"service": "StudyShop", "status": "ok", "example": "/calculate?price=100&quantity=3&discount=10"})

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/calculate")
    def calculate():
        try:
            price = int(request.args["price"])
            quantity = int(request.args["quantity"])
            discount = int(request.args.get("discount", "0"))
            result = total_cost(price, quantity, discount)
        except (KeyError, ValueError) as exc:
            return jsonify({"error": str(exc) or "Некорректные параметры"}), 400
        return jsonify({"total": result, "currency": "RUB"})

    return app


app = create_app()
