![Python](https://img.shields.io/badge/python-3.10-blue.svg)

# assembly-ai-pipe-and-transcript

Piping videos from popular providers (Youtube, Vimeo, etc...) to the [AssemblyAI API](https://www.assemblyai.com/docs) to extract audio and get transcriptions.

## Run this package locally

```bash
git clone {REPO_URL}
# optionally create your env 
# grab your API Key from https://www.assemblyai.com/
pip3 install -r requirements.txt
python3 main.py
```

## Usage

```python
from pipe_and_transcript import PipeAndTranscript

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=IOBQD41r4Wk'

# initialize the package
pipe = PipeAndTranscript(assembly_api_key='YOUR_API_KEY')

# transcript 
transcription = pipe.youtube.transcript(video_url=YOUTUBE_VIDEO_URL)

# pass additional transcription options
transcription = pipe.youtube.transcript(video_url=YOUTUBE_VIDEO_URL, speaker_labels=True)

# get response
transcription.response

# get text
transcription.text
```

## Notes
This project is far from being completed. Do expect bugs.