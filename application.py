from flask import Flask
from flask_cors import CORS
import json

from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
CORS(app)


def process_request(json_data: str, fn: function): # Error?
    try:
        inp = json.loads(json_data)
        ans = fn(inp)
        ans['input'] = inp
    except Exception as exc:
        ans = {'error': str(exc), 'input': json_data}

    return json.dumps(ans)


@app.route('/')
def welcome():
    return json.dumps({'message': 'Welcome from Reliability Measures!'})


@app.route('/std/<json_data>', methods=['POST', 'GET'])
def compute_std(json_data):
    return process_request(json_data, calculate_std)


@app.route('/summation/<json_data>', methods=['POST', 'GET'])
def compute_summation(json_data):
    return process_request(json_data, calculate_summation)


@app.route('/proportion/<json_data>', methods=['POST', 'GET'])
def compute_proportion(json_data):
    return process_request(json_data, calculate_proportion)


@app.route('/kr20/<json_data>', methods=['POST', 'GET'])
def compute_kr20(json_data):
    return process_request(json_data, calculate_kr20)


@app.route('/pbcc/<json_data>', methods=['POST', 'GET'])
def compute_pbcc(json_data):
    return process_request(json_data, calculate_proportion)


@app.route('/difficulty/<json_data>', methods=['POST', 'GET'])
def compute_difficulty(json_data):
    return process_request(json_data, calculate_difficulty)


@app.route('/scores/<json_data>', methods=['POST', 'GET'])
def compute_scores(json_data):
    return process_request(json_data, calculate_scores)


@app.route('/average/<json_data>', methods=['POST', 'GET'])
def compute_average(json_data):
    return process_request(json_data, calculate_average)


if __name__ == '__main__':
    app.run(threaded=True)