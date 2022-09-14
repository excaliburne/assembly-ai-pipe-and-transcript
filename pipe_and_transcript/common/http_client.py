# SYSTEM 
import requests, json
from typing import Union, Generator, Dict

# COMMON
from pipe_and_transcript.common.constants import ASSEMBLY_API_BASE_URL


class HttpClient:
    def __init__(self, api_key: str, base_url: str = ASSEMBLY_API_BASE_URL):
        self.api_key  = api_key
        self.base_url = base_url

    def make_request(self, method: str, endpoint: str, body: Union[Dict, Generator] = None) -> json:
        method = method.lower()
        args   = {}
        req    = getattr(requests, method)

        args['headers'] = {'authorization': self.api_key}

        if method == 'post':
            args['headers'] = {**args['headers'], 'Content-Type': 'application/json'}

        if body: 
            args['data'] = json.dumps(body) if type(body) is dict else body

        r: requests.Response = req(self.base_url + endpoint, **args)

        return r.json()