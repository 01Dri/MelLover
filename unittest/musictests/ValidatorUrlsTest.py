import unittest
from unittest.mock import Mock

from utils.utils_bot_music.ValidatorLinks import ValidatorUrls
from exception.UrlInvalidException import UrlInvalidException


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = Mock()

    def test_validate_url_youtube_pc(self):
        self.ctx.content = "addmusic https://www.youtube.com/watch?v=bMhiefW7WrQ&list=RDqf4OUzIjPQw&index=15"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://www.youtube.com/watch?v=bMhiefW7WrQ&list=RDqf4OUzIjPQw&index=15"
        self.assertEqual(url_expected, result)

    def test_validate_url_playlist_youtube_pc(self):
        self.ctx.content = "addmusic https://www.youtube.com/playlist?list=PLTGRYXB6q6-X-uQPm2STDtpShkN-UFF9R"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://www.youtube.com/playlist?list=PLTGRYXB6q6-X-uQPm2STDtpShkN-UFF9R"
        self.assertEqual(url_expected, result)

    def test_validate_url_youtube_mobal(self):
        self.ctx.content = "addmusic https://youtu.be/PgF29M69QXg?si=fp0TA-Sl1QBsmnVs"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://youtu.be/PgF29M69QXg?si=fp0TA-Sl1QBsmnVs"
        self.assertEqual(url_expected, result)

    def test_validate_url_playlist_youtube_mobal(self):
        self.ctx.content = "addmusic https://youtube.com/playlist?list=PLPzULCdMTsR-ARB4c5e08PioFwks16APQ&si=Wk2TYx5SvBvg1neK"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://youtube.com/playlist?list=PLPzULCdMTsR-ARB4c5e08PioFwks16APQ&si=Wk2TYx5SvBvg1neK"
        self.assertEqual(url_expected, result)

    def test_validate_url_spotify_pc(self):
        self.ctx.content = "addmusic https://open.spotify.com/intl-pt/track/5Rhrad2d6tLTG9hBSY0M3V?si=7dd06fd02db94602"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://open.spotify.com/intl-pt/track/5Rhrad2d6tLTG9hBSY0M3V?si=7dd06fd02db94602"
        self.assertEqual(url_expected, result)

    def test_validate_url_spotify_mobal(self):
        self.ctx.content = "addmusic https://spotify.link/rkADu3ek4Cb"
        validator_url = ValidatorUrls(self.ctx)
        result = validator_url.get_url_validated()
        url_expected = "https://spotify.link/rkADu3ek4Cb"
        self.assertEqual(url_expected, result)

    def test_error_validate_url(self):
        self.ctx.content = "addmusic testeserror"
        validator_url = ValidatorUrls(self.ctx)
        with self.assertRaises(UrlInvalidException):
            validator_url.get_url_validated()


if __name__ == '__main__':
    unittest.main()
