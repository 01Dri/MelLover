import asyncio

from utils.utils_bot_music.DownloaderMusicsFromYoutube import DownloaderYoutube


class Player:
    def __init__(self, client_voice, asyncio, pytube, manager_folder, discord, os):
        self.client_voice = client_voice
        self.asyncio = asyncio
        self.pytube = pytube
        self.manager_folder = manager_folder
        self.discord = discord
        self.os = os
        self.file = None
        self.skip_status = None
        self.i = 0
        self.queue = []

    async def play(self):
        while self.i < len(self.queue):
            downloader = DownloaderYoutube(self.queue[self.i], self.pytube, self.manager_folder, self.discord,
                                           self.os)
            self.file = await downloader.download()
            while self.client_voice.is_playing() or self.client_voice.is_paused():
                await asyncio.sleep(1)

            self.client_voice.play(self.file)
            self.i += 1

    def pause(self):
        self.client_voice.pause()

    def resume(self):
        self.client_voice.resume()

    def skip(self):
        self.client_voice.stop()
        pass

    async def stop(self):
        self.client_voice.stop()
        await self.client_voice.disconnect()
        await self.manager_folder.remove_folder_musics()
        pass
