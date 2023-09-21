import unittest
from unittest.mock import Mock, patch

from viewer.bot_music_viewer.EmbedErrors import EmbedErros
from viewer.bot_music_viewer.EmbedPlaylist import EmbedPlaylist
from viewer.bot_music_viewer.EmbedTrack import EmbedTrack


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.track = Mock()
        self.discord_account = Mock()
        self.playlist = Mock()

    @patch('discord.Embed')
    def test_embed_messages_solo_track(self, mock_discord_embed):
        # Attributos a serem usados
        self.track.url = ""
        self.track.name = "nome_test"
        self.track.time = 650
        self.discord_account.name = "drikill."
        self.discord_account.avatar_url = "teste.jpg"
        self.discord_account.server_id = 123

        embed = EmbedTrack(mock_discord_embed, self.track.name, self.track.time, self.discord_account.name,
                           self.discord_account.avatar_url)

        # Testes simples
        self.assertEqual("nome_test", embed.name_music)
        self.assertEqual(650, embed.length)
        self.assertEqual("drikill.", embed.author)
        self.assertEqual("teste.jpg", embed.author_image)

        # Verificando se a classe "Embed" do discord foi chamado no metodo get_embed
        embed.get_embed_for_add_musics()
        mock_discord_embed.called_once()

    @patch('discord.Embed')
    def test_embed_messages_playlist(self, mock_discord_embed):
        # Attributos a serem usados

        self.playlist.name = "playlist_nome"
        self.playlist.length = 25
        self.playlist.url = "url_teste"
        self.playlist.description = "teste"
        self.urls = ["url1", "url2"]

        self.discord_account.name = "drikill."
        self.discord_account.avatar_url = "teste.jpg"
        self.discord_account.server_id = 123

        embed = EmbedPlaylist(mock_discord_embed, self.playlist.name, self.playlist.description, self.playlist.length,
                              self.discord_account.name, self.discord_account.avatar_url)

        # Testes simples
        self.assertEqual("playlist_nome", embed.name_playlist)
        self.assertEqual(25, embed.amount_musics)
        self.assertEqual("teste", embed.description)
        self.assertEqual("drikill.", embed.author)
        self.assertEqual("teste.jpg", embed.author_image)

        # Verificando se a classe "Embed" do discord foi chamado no metodo get_embed
        embed.get_embed_for_add_playlist()
        mock_discord_embed.called_once()

    @patch('discord.Embed')
    def test_embed_error(self, mock_discord_embed):
        message = "mensagem de erro teste"
        embed = EmbedErros(mock_discord_embed, message)
        self.assertEqual("mensagem de erro teste", embed.message)
        embed.get_embed_error()
        mock_discord_embed.called_once()



if __name__ == '__main__':
    unittest.main()
