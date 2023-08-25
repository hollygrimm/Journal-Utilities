import unittest
import os
import sys

# Append the src directory to sys.path
sys.path.append("/mnt/md0/projects/Journal-Utilities/src")
from src.journalutils.get_audio import (
    download_mp4_pytube,
    download_mp4s_pytube,
    mp4_to_wav,
)
from src.journalutils import DATA_PATH


class TestGetAudio(unittest.TestCase):
    def test_download_mp4_pytube(self):
        video_url = "https://www.youtube.com/watch?v=k55mAFCIQ60"
        downloaded_filepath = download_mp4_pytube(video_url)
        self.assertIsNotNone(downloaded_filepath)

    def test_download_mp4s_pytube(self):
        video_urls = [
            "https://www.youtube.com/watch?v=TOZp_XNYijQ",
            "https://www.youtube.com/watch?v=k55mAFCIQ60",
        ]
        expected_downloaded_files = [
            "Physics as Information Processing  Chris Fields  Lecture 3.mp4",
            "Physics as Information Processing  Chris Fields  Lecture 4.mp4",
        ]
        downloaded_filepaths = download_mp4s_pytube(video_urls)
        downloaded_files = []
        for filepath in downloaded_filepaths:
            downloaded_files.append(os.path.basename(filepath))

        self.assertEqual(downloaded_files, expected_downloaded_files)

    def test_mp4_to_wav(self):
        mp4_filename = "Physics as Information Processing  Chris Fields  Lecture 4.mp4"
        wav_filename = mp4_filename.replace(".mp4", ".wav")

        input_file = DATA_PATH / "audio" / mp4_filename
        output_file = DATA_PATH / "audio" / wav_filename
        mp4_to_wav(input_file, output_file)

        self.assertTrue(output_file.exists())


if __name__ == "__main__":
    unittest.main()
