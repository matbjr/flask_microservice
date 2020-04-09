from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
import json
from config import get_config
from sample import sample, sample2

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
CORS(app)


def process_request(fn, json_data=None):
    """
    A function to convert a JSON formatted string to dict and
    then call the passed function and return the response.

    :param fn: a function to call
    :param json_data: str (optional in JSON format)
    :return: str, a JSON formatted string
    """
    pretty_json = 1
    try:
        pretty_json = request.args.get('pretty', pretty_json)
        if not json_data:
            json_data = request.args.get('input') or request.args.get('json')
        # print(pretty_json, json_data)
        inp = json.loads(json_data)
        ans = fn(inp)  # calling function 'fn'
        ans['Input'] = inp
    except Exception as exc:
        ans = {'error': str(exc), 'input': json_data}
    if pretty_json == 1:
        return jsonify(ans)
    else:
        return json.dumps(ans)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def welcome():
    return jsonify(
        {
            'message': 'Welcome from Reliability Measures!',
            'version': get_config('application_version')
        }
    )


@app.route('/std/', methods=['POST', 'GET'])
def compute_std():
    return process_request(calculate_std)


@app.route('/summation/', methods=['POST', 'GET'])
def compute_summation(json_data):
    return process_request(calculate_summation)


@app.route('/proportion/', methods=['POST', 'GET'])
def compute_proportion():
    return process_request( calculate_proportion)


@app.route('/kr20/', methods=['POST', 'GET'])
def compute_kr20():
    return process_request(calculate_kr20)


@app.route('/idr/', methods=['POST', 'GET'])
def compute_idr():
    return process_request( calculate_idr)


@app.route('/difficulty/', methods=['POST', 'GET'])
def compute_difficulty():
    return process_request( calculate_difficulty)


@app.route('/scores/', methods=['POST', 'GET'])
def compute_scores():
    return process_request( calculate_scores)


@app.route('/average/', methods=['POST', 'GET'])
def compute_average():
    return process_request( calculate_average)


@app.route('/analyzeTest/', methods=['POST', 'GET'])
@cross_origin()
def get_analysis():

    return process_request(analyze_test)


@app.route('/weightedScores/', methods=['POST', 'GET'])
def compute_weighted_scores():
    return process_request( calculate_weighted_scores)


@app.route('/weightedAverage/', methods=['POST', 'GET'])
def compute_weighted_avg():
    return process_request( calculate_weighted_average)


@app.route('/excludes/', methods=['POST', 'GET'])
def compute_excludes():
    return process_request( get_exclude_recos)


@app.route('/difficulty_avg/', methods=['POST', 'GET'])
def compute_diff_avg():
    return process_request( calculate_difficulty_average)


@app.route('/idr_avg/', methods=['POST', 'GET'])
def compute_idr_avg():
    return process_request( calculate_idr_average)


@app.route('/sample', methods=['POST', 'GET'])
@app.route('/sample/', methods=['POST', 'GET'])
@cross_origin()
def get_sample_analysis():
    return process_request(analyze_test, json.dumps(sample))


if __name__ == '__main__':
    print("Starting service")
    app.run(host="0.0.0.0", port=5000, threaded=True)

