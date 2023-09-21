import unittest

from unittest.mock import Mock, patch

from entities.DiscordAccount import DiscordAccount
from player.entities.Track import Track
from factory.SoloTrackYoutubeFactory import SoloTrackYoutubeFactory
from utils.utils_bot_music.ValidatorLinks import ValidatorUrls


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ctx = Mock()
        self.ctx.content = "addmusic https://www.youtube.com/watch?v=3Vn1xJluYPk"
        self.pytube_instance = Mock()
        self.discord_account = DiscordAccount("nome_teste", "teste.jpg", 123)
        self.validator = ValidatorUrls(self.ctx)

    @patch('pytube.YouTube')
    def test_create_instance_track_solo_youtube(self, mock_pytube):

        mock_pytube_instance = mock_pytube.return_value
        mock_pytube_instance.title = "Titulo do vídeo"
        mock_pytube_instance.length = 300

        factor_track_solo_youtube = SoloTrackYoutubeFactory(self.pytube_instance, self.discord_account, self.validator)
        result = factor_track_solo_youtube.get_instance_track_solo()
        self.assertIsInstance(result, Track)
        self.assertEqual(result.url, "https://www.youtube.com/watch?v=3Vn1xJluYPk")
        self.assertEqual(result.discord_account, self.discord_account)

if __name__ == '__main__':
    unittest.main()