from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
import json
import sys

from providers.google.get_credentials import GoogleCredentails
from providers.google.google_classroom import list_courses

from common.config import get_config, initialize_config
from common.sample import sample
from api.std import calculate_std
from api.summation import calculate_summation
from api.proportion import calculate_proportion
from api.kr20 import calculate_kr20
from api.idr import calculate_idr ,calculate_idr_average
from api.difficulty import calculate_difficulty, calculate_difficulty_average
from api.scores import calculate_scores, calculate_average
from api.analyze_test import analyze_test
from api.weighted_scores import calculate_weighted_scores, calculate_weighted_average
from api.excludes import get_exclude_recos
from api.num_correct import calculate_num_correct
from api.assumptions import get_assumptions
from api.analyze_grad_years import analyze_grad_years
from api.topic_rights import calculate_topic_rights, calculate_topic_averages


class RMApp(Flask):

    def __init__(self, *args, **kwargs):
        super(RMApp, self).__init__(*args, **kwargs)
        initialize_config()
        print(get_config("db_provider"))


app = RMApp(__name__)

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
        ans = {"error": str(exc), 'input': json_data}
    if pretty_json == 1:
        return jsonify(ans)
    else:
        return json.dumps(ans)


@app.route('/', methods=['POST', 'GET'])
def welcome():
    return jsonify(
        {
            "message": "Welcome from Reliability Measures!",
            "version": get_config('application_version'),
            'python_version': sys.version.split()[0]
        }
    )


@app.route('/login/', methods=['POST', 'GET'])
def get_tokens():
    id_token = request.args.get('id_token')
    access_token = request.args.get('access_token')
    app.gc = GoogleCredentails()
    creds, info = app.gc.get_credential_from_token(id_token, access_token)
    courses = list_courses(creds)
    #print(courses)
    return jsonify({'user': info, 'courses': courses})
    # return process_request(calculate_std)


@app.route('/classroom/', methods=['POST', 'GET'])
def get_classes():
    id_token = request.args.get('id_token')
    access_token = request.args.get('access_token')

    app.gc = GoogleCredentails()
    if access_token and id_token:
        creds, info = app.gc.get_credential_from_token(id_token, access_token)
    else:
        creds = app.gc.get_credential()  # RM organization courses
        info = {'name': get_config("application_org"),
                'email': get_config("application_email")}

    courses = list_courses(creds)
    #print(courses)
    return jsonify({'user': info, 'courses': courses})
    # return process_request(calculate_std)

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
    return process_request(calculate_difficulty)


@app.route('/scores/', methods=['POST', 'GET'])
def compute_scores():
    return process_request(calculate_scores)


@app.route('/average/', methods=['POST', 'GET'])
def compute_average():
    return process_request(calculate_average)


@app.route('/analyzeTest/', methods=['POST', 'GET'])
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


@app.route('/num_correct/', methods=['POST', 'GET'])
def compute_num_correct():
    return process_request( calculate_num_correct)


@app.route('/assumptions/', methods=['POST', 'GET'])
def compute_assumptions():
    return process_request( get_assumptions)


@app.route('/analyze_grad_years/', methods=['POST', 'GET'])
def get_grad_year_analysis():
    return process_request( analyze_grad_years)


@app.route('/topic_rights/', methods=['POST', 'GET'])
def get_topic_rights():
    return process_request( calculate_topic_rights)


@app.route('/topic_averages/', methods=['POST', 'GET'])
def get_topic_averages():
    return process_request( calculate_topic_averages)


@app.route('/sample', methods=['POST', 'GET'])
@app.route('/sample/', methods=['POST', 'GET'])
@cross_origin()
def get_sample_analysis():
    return process_request(analyze_test, json.dumps(sample))


if __name__ == '__main__':
    print("Starting service")
    app.run(host="0.0.0.0", port=5000, threaded=True)

