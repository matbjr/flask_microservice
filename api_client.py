from typing import Any
import json
from config import get_config
from sample import sample

api_url = get_config('test_url')


def call_service(url='localhost', method='', resp_key=None, **options: Any):
    import requests

    params = {}
    params.update(options)

    resp = requests.get(url + method, params=params)
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

    param = json.dumps(sample)
    resp = call_service(url=api_url, method='analyzeTest/', resp_key=None,
                 input=param)
    print(json.dumps(resp, indent=4))

    resp = call_service(url=api_url, method='sample', resp_key=None)
    print(json.dumps(resp, indent=4))