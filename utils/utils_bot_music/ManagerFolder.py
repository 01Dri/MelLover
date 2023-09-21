from exception.FolderPathMusicsNotExist import FolderPathMusicsNotExist
from exception.ServerIdDiscordNotFound import ServerIdDiscordNotFound


class ManagerFolders:

    def __init__(self, path, discord_account, os, asyncio, shutil):
        self.path = path
        self.discord_account = discord_account
        self.os = os
        self.asyncio = asyncio
        self.shutil = shutil
        pass

    def get_folder_path_for_musics(self):
        if self.discord_account.server_id is None:
            raise ServerIdDiscordNotFound("ID do servidor não localizado!")
        folder = f'{self.discord_account.server_id}'
        folder_full_path = self.os.path.join(self.path, folder)
        return folder_full_path

    def remove_mp4_before(self, name):
        self.os.remove(f'{name}.mp4')

    async def remove_folder_musics(self):
        await self.asyncio.sleep(5)
        try:
            print("chamou")
            self.shutil.rmtree(self.get_folder_path_for_musics())
            return True
        except:
            raise FolderPathMusicsNotExist("A pasta não existe!")
