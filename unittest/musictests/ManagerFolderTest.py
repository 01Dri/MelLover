import unittest
from unittest.mock import Mock, patch

from entities.DiscordAccount import DiscordAccount
from exception.ServerIdDiscordNotFound import ServerIdDiscordNotFound
from utils.utils_bot_music.ManagerFolder import ManagerFolders


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.discord_account = DiscordAccount("drikill", "teste.jpg", "123")
        self.path = "teste_folder/"
        self.os = Mock()
        self.asyncio = Mock()
        self.shutil = Mock()

    @patch('os.path.join')
    def test_manager_folder_get_folder_path(self, mock_os):
        mock_os_instance = mock_os.return_value
        mock_os_instance.path.join.return_value = self.path + self.discord_account.server_id
        manager = ManagerFolders(self.path, self.discord_account, mock_os_instance, self.asyncio, self.shutil)
        result = manager.get_folder_path_for_musics()
        self.assertEqual("teste_folder/123", result)

    @patch('os.path.join')
    def test_manager_folder_get_folder_path_exception_discord_id(self, mock_os):
        mock_os_instance = mock_os.return_value
        self.discord_account.server_id = ""
        mock_os_instance.path.join.return_value = self.path + self.discord_account.server_id
        manager = ManagerFolders(self.path, self.discord_account, mock_os_instance, self.asyncio, self.shutil)
        result = manager.get_folder_path_for_musics()
        self.assertRaises(ServerIdDiscordNotFound)

    @patch('asyncio.sleep')
    @patch('shutil.rmtree')
    async def test_manager_folder_remove_folder(self, mock_asyncio, mock_shutil):
        mock_asyncio_instance = mock_asyncio.return_value
        mock_shutil_instance = mock_shutil.return_value
        mock_asyncio_instance.sleep.return_value = 5
        mock_shutil_instance.rmtree.return_value = True
        manager = ManagerFolders(self.path, self.discord_account, self.os, self.asyncio, mock_shutil_instance)
        result = await manager.remove_folder_musics()
        mock_shutil_instance.rmtree.assert_called_once()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
