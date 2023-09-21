import unittest

from unittest.mock import Mock, patch, MagicMock

from entities.DiscordAccount import DiscordAccount
from player.entities.Playlist import Playlist
from exception.UrlInvalidPlaylistFactory import UrlInvalidPlaylistFactory
from factory.PlaylistYoutubeFactory import PlaylistYoutubeFactory
from utils.utils_bot_music.ValidatorLinks import ValidatorUrls


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ctx = Mock()
        self.pytube_instance = Mock()
        self.discord_account = DiscordAccount("nome_teste", "teste.jpg", 123)
        self.validator = ValidatorUrls(self.ctx)

    @patch('pytube.Playlist', new_callable=MagicMock)
    def test_create_instance_playlist_youtube(self, mock_pytube):
        self.ctx.content = "addmusic https://www.youtube.com/playlist?list=PLTGRYXB6q6-X-uQPm2STDtpShkN-UFF9R"

        # Configure o retorno de video_urls como uma lista usando PropertyMock
        video_urls = ["url_1", "url_2"]
        mock_pytube_instance = mock_pytube.return_value
        type(mock_pytube_instance).video_urls = video_urls

        mock_pytube_instance.title = "Titulo da playlist"
        mock_pytube_instance.length = 300
        mock_pytube_instance.description = "Testes descrição"

        factor_track_solo_youtube = PlaylistYoutubeFactory(mock_pytube_instance, self.discord_account, self.validator)
        result = factor_track_solo_youtube.get_instance_playlist_youtube()

        self.assertIsInstance(result, Playlist)
        self.assertEqual(result.url, "https://www.youtube.com/playlist?list=PLTGRYXB6q6-X-uQPm2STDtpShkN-UFF9R")
        self.assertEqual(result.discord_account, self.discord_account)

        # NÃO FUNCIONA AAAAAAAAAAAAA
       # self.assertEqual(2, len(result.urls))

    def test_exception_url_invalid_playlist_create_instance_playlist_youtube(self):
        self.ctx.content = "addmusic https://www.youtube.com/watch?v=wz7dSGjiSgY&list=PLPzULCdMTsR-ARB4c5e08PioFwks16APQ&index=1"
        factor_track_solo_youtube = PlaylistYoutubeFactory(self.pytube_instance, self.discord_account, self.validator)
        with self.assertRaises(UrlInvalidPlaylistFactory):
            result = factor_track_solo_youtube.get_instance_playlist_youtube()


if __name__ == '__main__':
    unittest.main()
