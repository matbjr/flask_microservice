import numpy as np
import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    return {'message': 'Welcome from Reliability Measures!'}


@app.route('/std/<json_array>', methods=['POST', 'GET'])
def compute_std(json_array):
    return calculate_std(json.loads(json_array))


def calculate_std(param):
    user_list = list(param['elements'])
    std_value = float(np.std(user_list))
    return {'Std': round(std_value, 3)}


app.run(port=8080, threaded=True)
