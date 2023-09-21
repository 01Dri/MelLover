

class DownloaderYoutube:

    def __init__(self, url, pytube, manager_folder, discord, os):
        self.url = url
        self.pytube = pytube
        self.manager_folder = manager_folder
        self.discord = discord
        self.os = os
        self.audio_stream = None
        pass

    async def download(self):
        pytube_video = self.pytube.YouTube(self.url)
        self.audio_stream = pytube_video.streams.filter(only_audio=True).first()
        self.audio_stream.download(self.manager_folder.get_folder_path_for_musics())
        audio_source_for_discord = self.discord.FFmpegPCMAudio(
            self.os.path.join(self.manager_folder.get_folder_path_for_musics(), self.audio_stream.default_filename))
        return audio_source_for_discord


# validator = ValidatorUrls("addmusic https://www.youtube.com/watch?v=idGkS085CoA")
# url = validator.get_url_validated()
# pytube = pytube
# discord_account = DiscordAccount("drikill.", "teste", "123456")
# manager_folder = ManagerFolders(DEFAULT_PATH_FOLDER_MUSICS, discord_account, os, asyncio, shutil)
# classe = DownloaderYoutube(url, pytube, manager_folder, discord, os)
# factory_track = SoloTrackYoutubeFactory(pytube, discord_account, validator)
# track_instance = factory_track.get_instance_track_solo()
# print(track_instance.url)
# classe.download()
