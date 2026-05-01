from flask import Flask, request, jsonify
from src.math_operations import add, sub


def create_app():
    app = Flask(__name__)

    @app.route("/add", methods=["GET"])
    def add_nums():
        try:
            a = float(request.args.get("a"))
            b = float(request.args.get("b"))
        except:
            return jsonify({"error": "Invalid Input"}), 400

        return jsonify({"result": add(a, b)})

    @app.route("/sub", methods=["GET"])
    def sub_nums():
        try:
            a = int(request.args.get("a"))
            b = int(request.args.get("b"))
        except:
            return jsonify({"error": "Invalid Input"}), 400

        return jsonify({"result": sub(a, b)})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
