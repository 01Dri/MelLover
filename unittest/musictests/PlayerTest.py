import unittest
from unittest.mock import Mock
from entities.DiscordAccount import DiscordAccount
from player.entities.Track import Track
from factory.SoloTrackYoutubeFactory import SoloTrackYoutubeFactory
from player.Player import Player

from utils.utils_bot_music.ValidatorLinks import ValidatorUrls


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.pytube = Mock()
        self.factory = Mock(spec=SoloTrackYoutubeFactory)
        self.discord_account = Mock(spec=DiscordAccount)
        self.discord_account.name = "Drikill."
        self.discord_account.avatar_url = "test.jpg"
        self.discord_account.server_id = "123"
        self.validator = Mock(spec=ValidatorUrls)

    def test_player_add_songs_track_solo_in_queue(self):
        self.validator.ctx = "addmusic https://www.youtube.com/watch?v=idGkS085CoA"
        factory_instance = SoloTrackYoutubeFactory(self.pytube, self.discord_account, self.validator)
        track = factory_instance.get_instance_track_solo()
        print(track)
        player = Player(track, None, None)
        self.assertIsInstance(track, Track)
        self.assertEqual(1, len(player.queue))


if __name__ == '__main__':
    unittest.main()
