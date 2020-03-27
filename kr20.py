import numpy as np 
import json

from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    return {'message': 'Hello'}


@app.route('/kr20/<json_array>', methods=['POST', 'GET'])
def compute_kr20(json_array):
    req = request.get_json(json_array)
    return calculate_kr20(req)


def calculate_kr20(param):
    student_list = list(param['students'])
    numStudents = len(student_list)
    numQ = len(student_list[0]['itemresponses'])
    for k in range(0, numStudents):
        if (numQ != len(student_list[k])):
            return {'Error: All student\'s item count must be the same'}
    pqList = []
    stdList = []
    for i in range(0, numQ):
        p = 0
        for k in range(0, numStudents):
            p += student_list[k]['itemresponses'][i]
        p /= numStudents
        pqList.append(p * (1-p))
    for k in range(0, numStudents):
        stdList.append(sum(student_list[k]['itemresponses']))
    kr20_value = (numQ/(numQ - 1)) * (1 - (sum(pqList)/np.std(stdList)**2))
    return {'kr20': round(kr20_value, 3)}


app.run()