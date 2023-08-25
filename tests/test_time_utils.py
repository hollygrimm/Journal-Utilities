import unittest
from src.journalutils.time_utils import to_display_time, to_srt_time


class TimeTests(unittest.TestCase):
    def test_positive_hours(self):
        self.assertEqual(to_display_time(3600000), "1:00:00")
        self.assertEqual(to_display_time(7200000), "2:00:00")
        self.assertEqual(to_display_time(10800000), "3:00:00")

    def test_single_digit_hours(self):
        self.assertEqual(to_display_time(600000), "10:00")
        self.assertEqual(to_display_time(1200000), "20:00")
        self.assertEqual(to_display_time(1800000), "30:00")

    def test_minutes_and_seconds(self):
        self.assertEqual(to_display_time(60000), "01:00")
        self.assertEqual(to_display_time(120000), "02:00")
        self.assertEqual(to_display_time(180000), "03:00")
        self.assertEqual(to_display_time(1000), "00:01")
        self.assertEqual(to_display_time(2000), "00:02")
        self.assertEqual(to_display_time(3000), "00:03")

    def test_srt_positive_hours(self):
        self.assertEqual(to_srt_time(3600000), "01:00:00,000")
        self.assertEqual(to_srt_time(7200000), "02:00:00,000")
        self.assertEqual(to_srt_time(10800000), "03:00:00,000")

    def test_srt_single_digit_hours(self):
        self.assertEqual(to_srt_time(600000), "00:10:00,410")
        self.assertEqual(to_srt_time(1200000), "00:20:00,081")
        self.assertEqual(to_srt_time(1800000), "00:30:00,621")

    def test_srt_minutes_and_seconds(self):
        self.assertEqual(to_srt_time(60000), "00:01:00,500")
        self.assertEqual(to_srt_time(120000), "00:02:00,090")
        self.assertEqual(to_srt_time(180000), "00:03:00,630")
        self.assertEqual(to_srt_time(1000), "00:00:01,999")
        self.assertEqual(to_srt_time(2000), "00:00:02,998")
        self.assertEqual(to_srt_time(3000), "00:00:03,997")
        self.assertEqual(to_srt_time(1234), "00:00:01,233")
        self.assertEqual(to_srt_time(5678), "00:00:05,673")


if __name__ == "__main__":
    unittest.main()
