# MODULES
from pipe_and_transcript.modules import Youtube, Vimeo


class PipeAndTranscript:
    def __init__(self, assembly_api_key: str):
        self.assembly_api_key = assembly_api_key

        self._sdk_params = {
            'assembly_api_key': assembly_api_key,
        }

        self.youtube = Youtube(**self._sdk_params)
        self.vimeo   = Vimeo(**self._sdk_params)