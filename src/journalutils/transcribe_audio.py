import os
import time
import requests
from dotenv import load_dotenv
import whisper
from journalutils import DATA_PATH
from journalutils.get_audio import download_mp4_pytube, mp4_to_wav
import assemblyai as aai

def transcribe_audio_assemblyai(audio_url):
    # 
    # args:
    # audio_url: str - could be a local file path or a url
    #
    # returns transcript as form:
    # {
    #     id:"63ue03ne5b-2429-48ec-9cdb-f64204680dd1",
    #     status:"completed",
    #     audio_url:"https://cdn.assemblyai.com/upload/4db7fbe4-be9e-4b62-867b-6b818bb76f8a",
    #     text:""You. Hello and welcome, everyone. It's July 13, 2023...",
    #     words:[...],
    #     utterances:None,
    #     confidence:0.956467685185185,
    #     audio_duration:60.0,
    # }
    load_dotenv()
    aai.settings.api_key = os.getenv('ASSEMBLYAI_AUTH_KEY')
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_url)
    return transcript

    
def transcribe_audio_with_whisper(video_url) -> str:
    # Start the timer
    tic = time.perf_counter()

    # Download the audio from the YouTube video
    downloaded_filepath = download_mp4_pytube(video_url)

    mp4_filename = os.path.basename(downloaded_filepath)
    wav_filename = mp4_filename.replace(".mp4", ".wav")
    txt_filename = mp4_filename.replace(".mp4", ".txt")

    # Convert the downloaded MP4 file to WAV format
    mp4_to_wav(DATA_PATH / "audio" / mp4_filename, DATA_PATH / "audio" / wav_filename)

    # Load the Automatic Speech Recognition (ASR) model
    whisper_model = whisper.load_model("base.en")

    # Transcribe the audio file
    result = whisper_model.transcribe(str(DATA_PATH / "audio" / wav_filename))

    # Write the transcription to a text file
    transcript_filepath = DATA_PATH / "transcripts" / txt_filename
    with open(transcript_filepath, "w", encoding="UTF-8") as file:
        file.write(result["text"])

    # Stop the timer and calculate the total time taken
    toc = time.perf_counter()
    print(f"Total time taken: {toc - tic}")

    return transcript_filepath
