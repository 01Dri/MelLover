from discord.ext import commands

from discord.flags import Intents
from dotenv import load_dotenv

from constants.Constants import DEFAULT_PATH_FOLDER_MUSICS
from entities.DiscordAccount import DiscordAccount
from exception.AuthorIsNotConnectedInChannel import AuthorIsNotConnectedInChannel
from exception.UrlInvalidException import UrlInvalidException
from exception.UrlInvalidPlaylistFactory import UrlInvalidPlaylistFactory
from handler.handler_embeds_messages.HandlerErrorsMessage import HandlerErrorsMessages
from handler.handler_embeds_messages.HandlerMessagesPlaylist import HandlerMessagePlaylist
from handler.handler_embeds_messages.HandlerMessagesSoloTrack import HandlerMessagesSoloTrack
from player.entities.Playlist import Playlist
from player.entities.Track import Track

from utils.utils_bot_music.ConnectorBotCall import ConnectorBot
from utils.utils_bot_music.ManagerFolder import ManagerFolders
from utils.utils_bot_music.ValidatorLinks import ValidatorUrls

from handler.HandlerPlayer import HandlerPlayer

import asyncio
import os
import discord
import shutil


class DiscordBot(commands.Bot):

    def __init__(self, intents: Intents) -> None:
        super().__init__(command_prefix="!", intents=intents)
        self.server_players = {}
        self.player = None
        self.client_voice = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!play"):
            global handler_messages_solo_track, handler, validate
            server_id = message.guild.id
            try:
                connector = ConnectorBot(message, discord)
                connector.get_voice_channel()
                validate = ValidatorUrls(message).get_url_validated()
                discord_account = DiscordAccount(message.author, message.author.display_avatar, server_id)
                try:
                    self.client_voice = await connector.get_voice_client()
                except:
                    pass
                manager_folder = ManagerFolders(DEFAULT_PATH_FOLDER_MUSICS, discord_account, os, asyncio, shutil)

                handler = HandlerPlayer(server_id, validate, discord_account, connector, manager_folder, message,
                                        self.server_players, asyncio, os, self.client_voice)

                player = await handler.init_player()

                if isinstance(handler.get_entity(), Track):
                    handler_messages_solo_track = HandlerMessagesSoloTrack(discord, handler.get_entity(),
                                                                           discord_account)
                    await message.reply(embed=handler_messages_solo_track.send_message_for_track_add())

                if isinstance(handler.get_entity(), Playlist):
                    handler_messages_playlist = HandlerMessagePlaylist(discord, handler.get_entity(), discord_account)
                    await message.reply(embed=handler_messages_playlist.send_message_for_add_playlist())

                await player.play()
                await message.channel.send(embed=handler_messages_solo_track.send_message_for_current_track())

            except AuthorIsNotConnectedInChannel as e:
                handler_error = HandlerErrorsMessages(discord, e)
                await message.reply(embed=handler_error.send_message_error_emebed())

            except UrlInvalidException as e:
                handler_error = HandlerErrorsMessages(discord, e)
                await message.reply(embed=handler_error.send_message_error_emebed())

            except UrlInvalidPlaylistFactory as e:
                handler_error = HandlerErrorsMessages(discord, e)
                await message.reply(embed=handler_error.send_message_error_emebed())

            # Tratando o erro de forma genérica, preciso ajustar dps
            except Exception as e:
                handler_error = HandlerErrorsMessages(discord, "Falha ao tentar localizar a música")
                await message.reply(embed=handler_error.send_message_error_emebed())

        if message.content.startswith("!pause"):
            server_id = message.guild.id
            if server_id in self.server_players:
                player = self.server_players[server_id]
                player.pause()

        if message.content.startswith("!resume"):
            server_id = message.guild.id
            if server_id in self.server_players:
                player = self.server_players[server_id]
                player.resume()

        if message.content.startswith("!skip"):
            server_id = message.guild.id
            if server_id in self.server_players:
                player = self.server_players[server_id]
                player.skip()

        if message.content.startswith("!stop"):
            server_id = message.guild.id
            if server_id in self.server_players:
                player = self.server_players[server_id]
                await player.stop()


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = DiscordBot(intents=intents)
bot.run(os.getenv("TOKEN_DISCORD"))
