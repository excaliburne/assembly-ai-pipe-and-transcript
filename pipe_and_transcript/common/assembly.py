# SYSTEM
from typing import Union, List

# COMMON
from pipe_and_transcript.common import MakeAssemblyRequest

# UTILS
from pipe_and_transcript.utils import Oss


class Assembly:
    def __init__(self, api_key: str, audio_file_path: str = None, audio_url: str = None):
        self.api_key   = api_key
        self.audio_url = audio_url
        self.audio_file_path = audio_file_path
        
        self.transcript_id = None
    
    def is_transcription_done(self, transcript_id: str) -> bool:
        """
        Checks if transcription status is "completed"

        Args:
            transcript_id (str)

        Returns:
            (bool)
        """
        transcript_id: str = transcript_id or self.transcript_id
        response: MakeAssemblyRequest = self.get_transcription(transcript_id)

        return response.transcript_status == 'completed'

    def upload(self, audio_file_path: str = None):
        """
        Uploads a local audio file to AssemblyAI

        Args:
            audio_file_path (str, optional): Defaults to None. Refers to self.audio_file_path if None.

        Returns:
            (MakeAssemblyRequest)
        """
        audio_file_path = audio_file_path or self.audio_file_path

        response = MakeAssemblyRequest(
            endpoint_key="upload",
            method="POST",
            api_key=self.api_key,
            json_body=Oss.read_file(audio_file_path)
        )

        return response

    def transcript(
        self, 
        audio_url: str = None,
        **transcript_options
        ):
        """
        Starts audio transcription by calling AssemblyAI's /v2/transcript endpoint

        Args:
            audio_url (str, optional): Defaults to None. Refers to self.audio_url if None
            speaker_labels (bool, optional): Defaults to False.
                https://www.assemblyai.com/docs/core-transcription#speaker-labels-speaker-diarization
            word_boost(list, optional). Defaults to None. 
                https://www.assemblyai.com/docs/core-transcription#custom-vocabulary
                
        Returns:
            (MakeAssemblyRequest)
        """
        audio_url = audio_url or self.audio_url

        response = MakeAssemblyRequest(
            endpoint_key="transcript",
            method="POST",
            api_key=self.api_key,
            json_body={
                'audio_url': audio_url,
                **({'speaker_labels': True} if transcript_options.get('speaker_labels') else {}),
                **({'word_boost': transcript_options.get('word_boost')} if transcript_options.get('word_boost') else {}),
                **({'filter_profanity': True} if transcript_options.get('filter_profanity') else {})
            }
        )

        return response
    
    def get_transcription(self, transcript_id: str):
        """
        Get AssemblyAI transcription by id.

        Args:
            transcript_id (str)

        Returns:
            (MakeAssemblyRequest)
        """
        transcript_id: str = transcript_id or self.transcript_id

        response = MakeAssemblyRequest(
            endpoint_key="transcript__get",
            method="GET",
            api_key=self.api_key,
            path_variables={'transcript_id': transcript_id}
        )

        return response

