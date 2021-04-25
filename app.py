from flask import Flask, render_template, jsonify, request
import json
import data as fn


app = Flask(__name__)
PORT = 4000


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {
        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")


'''
http://0.0.0.0:3000/api/data
'''


@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = fn.get_data()
    return jsonify(result)


'''
http://0.0.0.0:3000/api/add
http://0.0.0.0:3000/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''


@app.route("/api/add", methods=["GET"])
def api_add_data():
    food = request.values.get('food')
    carbohydrates = request.values.get('carbohydrates')
    protein = request.values.get('protein')
    fat = request.values.get('fat')

    result = {
        'food': food,
        'carbohydrates': carbohydrates,
        'protein': protein,
        'fat': fat

    }
    result_data = fn.add_row(food, carbohydrates, protein, fat)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
