from flask import Flask
import json

from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route('/')
def welcome():
    return json.dumps({'message': 'Welcome from Reliability Measures!'})


@app.route('/std/<json_array>', methods=['POST', 'GET'])
def compute_std(json_array):
    inp = json.loads(json_array)
    ans = calculate_std(inp)
    ans['input'] = inp
    return json.dumps(ans)


@app.route('/summation/<json_array>', methods=['POST', 'GET'])
def compute_summation(json_array):
    inp = json.loads(json_array)
    ans = calculate_summation(inp)
    ans['input'] = inp
    return json.dumps(ans)


@app.route('/proportion/<json_array>', methods=['POST', 'GET'])
def compute_proportion(json_array):
    inp = json.loads(json_array)
    ans = calculate_proportion(inp)
    ans['input'] = inp
    return json.dumps(ans)


@app.route('/kr20/<json_array>', methods=['POST', 'GET'])
def compute_kr20(json_array):
    inp = json.loads(json_array)
    ans = calculate_kr20(inp)
    ans['input'] = inp
    return json.dumps(ans)


if __name__ == '__main__':
    app.run(threaded=True)
