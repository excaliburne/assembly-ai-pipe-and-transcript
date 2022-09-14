# SYSTEM
from time   import sleep
from typing import List, Union

# PACKAGES
import youtube_dl

# COMMONS
from pipe_and_transcript.common import Assembly, Paths, MakeAssemblyRequest
from pipe_and_transcript.common.constants import PIPED_AUDIO_NAME, SECONDS_BETWEEN_TRANSCRIPT_STATUS_CHECK

# UTILS
from pipe_and_transcript.utils.decorators import delete_temp_file_on_completion
from pipe_and_transcript.utils.dicts      import Dicts


class Youtube:
    def __init__(self, assembly_api_key: str):
        self.assembly_api_key = assembly_api_key

    def _download_video(self, video_url: str) -> bool:
        """
        Downloads a youtube video, extract the audio only then place the file under the temp/ directory

        Args:
            video_url (str): A valid youtube video url

        Returns:
            (str): The temp file name
        """
        video_info = youtube_dl.YoutubeDL().extract_info(video_url, download=False)
        filename   = f"{Paths.TEMP_DIRECTORY}/{PIPED_AUDIO_NAME}.mp3"
        options = {
            'format':'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        return filename
    
    @delete_temp_file_on_completion('audio1.mp3')
    def transcript(
        self, 
        video_url: str,
        speaker_labels: bool = False,
        word_boost: Union[List[str], None] = None,
        filter_profanity: bool = False
        ) -> dict:
        """
        Transcript a youtube video

        Args:
            video_url (str): A valid youtube video url
            speaker_labels (bool, optional): Defaults to False.
                https://www.assemblyai.com/docs/core-transcription#speaker-labels-speaker-diarization
            word_boost(list, optional). Defaults to None. 
                https://www.assemblyai.com/docs/core-transcription#custom-vocabulary
            filter_profanity(bool, optional). Defaults to False.
                https://www.assemblyai.com/docs/core-transcription#profanity-filtering

        Returns:
            (MakeAssemblyRequest): Assembly /v2/transcript response wrapped in a MakeAssemblyRequest object
                ...See response schema in data/json/response.transcript.json and MakeAssemblyRequest object for fields you can query
        """

        transcript_options = Dicts(locals().items()).filter_keys(['self', 'video_url'])

        audio_file_path: str = self._download_video(video_url)
        assembly = Assembly(self.assembly_api_key, audio_file_path)
        
        upload_response     = assembly.upload()
        transcript_response = assembly.transcript(audio_url=upload_response.upload_url, **transcript_options)

        while not assembly.is_transcription_done(transcript_response.transcript_id):
            print('Not done!')
            sleep(SECONDS_BETWEEN_TRANSCRIPT_STATUS_CHECK)

        return assembly.get_transcription(transcript_response.transcript_id)
    