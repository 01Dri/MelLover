from exception.UrlInvalidException import UrlInvalidException
from player.entities.Track import Track


class SoloTrackYoutubeFactory:

    def __init__(self, pytube_instance, discord_account, validator_links):
        self.pytube_instance = pytube_instance
        self.discord_account = discord_account
        self.validator = validator_links
        self.urls_list = []

    def get_instance_track_solo(self):
        url = self.validator.get_url_validated()
        print(url)
        if url is None:
            raise UrlInvalidException("Url inválido!")
        else:

            video_youtube = self.pytube_instance.YouTube(url)
            self.urls_list.append(url)
            track = Track(video_youtube.title, video_youtube.length, self.discord_account, url, self.urls_list)

            print(track.urls)
            return track

