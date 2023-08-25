import unittest
import sys
from unittest.mock import patch

# Append the src directory to sys.path
sys.path.append("/mnt/md0/projects/Journal-Utilities/src")
from src.journalutils.transcribe_audio import transcribe_audio_with_whisper
from src.journalutils import DATA_PATH


class TestTranscribeAudio(unittest.TestCase):
    def test_transcribe_audio_with_whisper(self):
        video_url = "https://www.youtube.com/watch?v=k55mAFCIQ60"
        transcript_filepath = transcribe_audio_with_whisper(video_url)
        self.assertTrue(transcript_filepath.exists())

    # @patch("journalutils.transcribe_audio.download_mp4_pytube")
    # @patch("journalutils.transcribe_audio.mp4_to_wav")
    # def test_transcribe_audio_with_whisper_mock(self, mock_download_mp4_pytube, mock_mp4_to_wav):
    #     video_url = "https://www.youtube.com/watch?v=k55mAFCIQ60"

    #     # Set up mock return values
    #     mock_download_mp4_pytube.return_value = "/mnt/md0/projects/Journal-Utilities/data/audio/Physics as Information Processing  Chris Fields  Lecture 4.mp4"

    #     # Call the function to be tested
    #     transcribe_audio_with_whisper("https://www.youtube.com/watch?v=video_id")

    #     # Assert that the function calls were made correctly
    #     mock_download_mp4_pytube.assert_called_once_with(video_url)
    #     mock_mp4_to_wav.assert_called_once_with("/mnt/md0/projects/Journal-Utilities/data/audio/Physics as Information Processing  Chris Fields  Lecture 4.mp4", "/mnt/md0/projects/Journal-Utilities/data/audio/Physics as Information Processing  Chris Fields  Lecture 4.wav")
