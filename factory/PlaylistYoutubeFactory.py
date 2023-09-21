from player.entities.Playlist import Playlist
from exception.UrlInvalidException import UrlInvalidException

from exception.UrlInvalidPlaylistFactory import UrlInvalidPlaylistFactory


class PlaylistYoutubeFactory:

    def __init__(self, pytube, discord_account, validator_links):
        self.pytube = pytube
        self.discord_account = discord_account
        self.validator_links = validator_links
        self.urls = []
        self.guid_musicas = {}
        self.playlist_desc = None
        self.playlist_youtube = None

    def get_instance_playlist_youtube(self):
        url = self.validator_links.get_url_validated()
        print(url)
        if not "https://www.youtube.com/playlist" in url:
            raise UrlInvalidPlaylistFactory("Url informado não pertence a uma playlist.")
        if url is None:
            raise UrlInvalidException("Url inválido!")
        self.playlist_youtube = self.pytube.Playlist(url)

        try:
            self.playlist_desc = self.playlist_youtube.description
        except:
            self.playlist_desc = "Sem descrição"

        for track in self.playlist_youtube.video_urls:
            self.urls.append(track)

        playlist = Playlist(self.playlist_youtube.title, self.playlist_youtube.length, url, self.playlist_desc,
                            self.urls,
                            self.discord_account)
        print(playlist.urls)
        print(f'teste {playlist}')
        return playlist

# discord = DiscordAccount("drikill.", "teste", "123")
# validator = ValidatorUrls("addmusic https://www.youtube.com/playlist?list=PLPzULCdMTsR-ARB4c5e08PioFwks16APQ")
# factory = PlaylistYoutubeFactory(pytube, discord, validator)
# entity = factory.get_instance_playlist_youtube()
# print(entity)
# print(entity.urls)
# print(entity.name)
