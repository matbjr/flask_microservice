from flask import Flask, jsonify
from flask_cors import cross_origin
import json
from utils import get_config
from sample import sample

from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from idr import calculate_idr
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from analyze_test import analyze_test
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
from excludes import get_exclude_recos
from difficulty_average import calculate_difficulty_average
from idr_average import calculate_idr_average


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


def process_request(json_data: str, fn):
    """
    A function to convert a JSON formatted string to dict and
    then call the passed function and return the response.

    :param json_data: str (in JSON format)
    :param fn: a function to call
    :return: str, a JSON formatted string
    """

    try:
        inp = json.loads(json_data)
        ans = fn(inp)  # calling function 'fn'
        ans['Input'] = inp
    except Exception as exc:
        ans = {'error': str(exc), 'input': json_data}

    return jsonify(ans)


@app.route('/')
@cross_origin()
def welcome():
    return jsonify({'message': 'Welcome from Reliability Measures!',
                    'version': get_config('application_version')})


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


@app.route('/idr/<json_data>', methods=['POST', 'GET'])
def compute_idr(json_data):
    return process_request(json_data, calculate_idr)


@app.route('/difficulty/<json_data>', methods=['POST', 'GET'])
def compute_difficulty(json_data):
    return process_request(json_data, calculate_difficulty)


@app.route('/scores/<json_data>', methods=['POST', 'GET'])
def compute_scores(json_data):
    return process_request(json_data, calculate_scores)


@app.route('/average/<json_data>', methods=['POST', 'GET'])
def compute_average(json_data):
    return process_request(json_data, calculate_average)


@app.route('/analyzeTest/<json_data>', methods=['POST', 'GET'])
@cross_origin()
def get_analysis(json_data):
    return process_request(json_data, analyze_test)


@app.route('/weightedScores/<json_data>', methods=['POST', 'GET'])
def compute_weighted_scores(json_data):
    return process_request(json_data, calculate_weighted_scores)


@app.route('/weightedAverage/<json_data>', methods=['POST', 'GET'])
def compute_weighted_avg(json_data):
    return process_request(json_data, calculate_weighted_average)


@app.route('/excludes/<json_data>', methods=['POST', 'GET'])
def compute_excludes(json_data):
    return process_request(json_data, get_exclude_recos)


@app.route('/difficulty_avg/<json_data>', methods=['POST', 'GET'])
def compute_diff_avg(json_data):
    return process_request(json_data, calculate_difficulty_average)


@app.route('/idr_avg/<json_data>', methods=['POST', 'GET'])
def compute_idr_avg(json_data):
    return process_request(json_data, calculate_idr_average)


@app.route('/sample', methods=['POST', 'GET'])
@cross_origin()
def get_sample_analysis():
    return process_request(json.dumps(sample), analyze_test_scores)


if __name__ == '__main__':
    print("Starting service")
    app.run(host="0.0.0.0", port=8000, threaded=True)

