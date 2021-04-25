from flask import Flask, render_template, jsonify, request
import json
import data as fn
import os


app = Flask(__name__)
PORT = int(os.environ.get('PORT', 3000))


@app.route("/", methods=["GET", "POST"])
def startpy():

    return render_template("index.html")


@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = fn.get_data()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
