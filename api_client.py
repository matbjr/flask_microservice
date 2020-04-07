import json
from utils import get_config

api_url = get_config('service_url')


def call_service(url='localhost', method='', param=None, resp_key=None):
    import requests

    if isinstance(param, dict):
        param = json.dumps(param)
    if param is None or not isinstance(param, str):
        param = ''

    resp = requests.get(url + method + param)
    if resp.status_code == 200:
        data = resp.json()
        if resp_key:
            return data.get(resp_key)
        else:
            return data
    else:
        return {'error': str(resp.status_code) + " " + resp.reason}


def get_std(scores: list):
    return call_service(url=api_url, method='std/',
                 param={"elements": scores}, resp_key='std')


def get_kr20(scores: dict):
    return call_service(url=api_url, method='kr20/',
                 param=scores, resp_key='kr20')


def get_idr(scores: dict):
    return call_service(url=api_url, method='idr/',
                 param=scores, resp_key='idr')


if __name__ == '__main__':

    param = {"elements": [4, 5.6, 7, 0, 22, -4.5]}
    print(call_service(url=api_url, method='std/',
                       param=param))

    print(get_std(param['elements']))

    data2 = {
        "students": [
            {"itemresponses": [1, 0, 1, 1, 0, 1]},
            {"itemresponses": [0, 1, 1, 1, 1, 1]},
            {"itemresponses": [0, 1, 0, 0, 0, 1]},
            {"itemresponses": [1, 1, 1, 1, 1, 1]},
            {"itemresponses": [0, 0, 0, 0, 1, 0]}
        ]
    }

    data = {
        "students":  [
            {"itemresponses": [ 1, 1, 1, 0 ]},
            {"itemresponses": [ 0, 1, 0, 1 ]}
         ]
    }

    print(get_kr20(data))
    print(get_idr(data))
