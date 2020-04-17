from typing import Any
import json
from api.config import get_config
from sample import sample, sample2

api_url = get_config('service_url')


def call_service(url='localhost', method='', resp_key=None, **options: Any):
    import requests

    params = {}
    params.update(options)

    resp = requests.post(url + method, params=params)
    if resp.status_code == 200:
        print(resp.content)
        data = resp.json()
        if resp_key:
            return data.get(resp_key)
        else:
            return data
    else:
        return {"error": str(resp.status_code) + " " + resp.reason}


def get_std(scores: list):
    return call_service(url=api_url, method='std/',
                 param={"elements": scores}, resp_key='std')


def get_kr20(scores: dict):
    return call_service(url=api_url, method='kr20/',
                 resp_key='kr20', pretty=1, input=param)


def get_idr(scores: dict):
    return call_service(url=api_url, method='idr/',
                 param=scores, resp_key='idr')


if __name__ == '__main__':

    resp = call_service(url=api_url, method='', resp_key=None)
    print(json.dumps(resp, indent=4))

    resp = call_service(url=api_url, method='sample', resp_key=None, pretty=1)
    print(json.dumps(resp, indent=4))

    param = json.dumps(sample2)
    resp = call_service(url=api_url, method='kr20/', resp_key=None,
                        pretty=1, input=param)
    print(json.dumps(resp, indent=4))


