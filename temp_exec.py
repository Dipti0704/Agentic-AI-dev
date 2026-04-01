# ENTRY_POINT: /
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"message": "Hello from API"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)