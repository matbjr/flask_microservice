from flask import Flask
from flask_cors import CORS
import json

from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20

app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    return {'message': 'Welcome from Reliability Measures!'}


@app.route('/std/<json_array>', methods=['POST', 'GET'])
def compute_std(json_array):
    print(json_array)
    return calculate_std(json.loads(json_array))


@app.route('/summation/<json_array>', methods=['POST', 'GET'])
def compute_summation(json_array):
    return calculate_summation(json.loads(json_array))


@app.route('/proportion/<json_array>', methods=['POST', 'GET'])
def compute_proportion(json_array):

    return calculate_proportion(json.loads(json_array))


@app.route('/kr20/<json_array>', methods=['POST', 'GET'])
def compute_kr20(json_array):
    return calculate_kr20(json.loads(json_array))


app.run(port=8082, threaded=True)
