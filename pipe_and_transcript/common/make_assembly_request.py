# COMMON
from pipe_and_transcript.common import HttpClient

# UTILS
from pipe_and_transcript.utils import UrlHandler


class MakeAssemblyRequest:
    def __init__(
        self, 
        endpoint_key: str, 
        method: str, 
        api_key: str, 
        path_variables: dict = None,
        query_params: dict = None,
        json_body: dict = None
        ):
        self._endpoint     = UrlHandler.build(
            endpoint_key,
            **({'path_variables': path_variables} if path_variables else {}),
            **({'query_params': query_params} if query_params else {})
        )
        self._method       = method
        self._api_key      = api_key
        self._json_body    = json_body

        # can query
        self.response = None
        self.transcript_status = None
        self.transcript_id     = None
        self.upload_url        = None
        self.text = None

        self.make_request()
    
    def make_request(self):
        response = HttpClient(self._api_key).make_request(
            endpoint=self._endpoint,
            method=self._method,
            **({'body': self._json_body} if self._json_body else {})
        )

        self.response = response
        self.transcript_status = response.get('status')
        self.transcript_id     = response.get('id')
        self.upload_url        = response.get('upload_url')
        self.text              = response.get('text')