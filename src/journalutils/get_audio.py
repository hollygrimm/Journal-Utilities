from typing import List
import pytube
import moviepy.editor as mp
from journalutils import DATA_PATH


def download_mp4_pytube(video_url) -> str:
    """
    Function to download the audio from a YouTube video.

    Parameters:
    video_url (str): The URL of the YouTube video.

    Returns:
    str: The path to the downloaded file.
    """
    # Initialize a YouTube object with the video URL
    data = pytube.YouTube(video_url)

    # Get the audio only stream
    audio = data.streams.get_audio_only()

    # Download the audio file and return the path to the file
    downloaded_filepath = audio.download(output_path=DATA_PATH / "audio")
    return downloaded_filepath


def download_mp4s_pytube(video_urls: List[str]) -> List[str]:
    downloaded_files = []
    for video_url in video_urls:
        downloaded_files.append(download_mp4_pytube(video_url))

    return downloaded_files


# def download_m4a_yt_dlp(video_url) -> str:
#     ''' Takes in a video_url
#     returns downloaded file path
#     '''
#     ydl_opts = {
#         'format': 'm4a/bestaudio/best',
#         # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their
#         'postprocessors': [{  # Extract audio using ffmpeg
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'm4a',
#         }],
#         "external_downloader_args": ['-loglevel', 'panic'],
#         "quiet": True,
#         'outtmpl': str(DATA_PATH / "audio") + "/%(title)s.%(ext)s",
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         try:
#             downloaded_filepath = ydl.download(video_url)
#         except yt_dlp.utils.DownloadError as error:
#             print(error)

#     return downloaded_filepath


def mp4_to_wav(input_filepath, output_filepath):
    """
    Function to convert an MP4 file to WAV format.

    Parameters:
    input_file (str): The path to the input MP4 file.
    output_file (str): The path to the output WAV file.
    """
    # Load the audio file
    audio = mp.AudioFileClip(str(input_filepath))

    # Write the audio file in WAV format
    audio.write_audiofile(str(output_filepath), codec="pcm_s16le")
