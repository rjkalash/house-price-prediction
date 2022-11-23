from pickle import GET
import re
from types import GenericAlias
from flask import Flask, request, jsonify
from werkzeug.wrappers import response
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST', 'GET'])
def predict_home_price():
    if request.method == 'GET':
        print('This is also good, People using GET in POST')
        return 'OKK , do whatever you like'
    total_sqft = float(request.form['total_sqft'])
    location = str(request.form['location'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server for Home Price Prediction...")
    app.run()
