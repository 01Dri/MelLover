import pytube
import discord

from player.entities.Playlist import Playlist
from player.entities.Track import Track
from factory.PlaylistYoutubeFactory import PlaylistYoutubeFactory
from factory.SoloTrackYoutubeFactory import SoloTrackYoutubeFactory
from player.Player import Player


class HandlerPlayer:

    def __init__(self, server_id, validator, discord_account, connector, manager, message, server_players, asyncio, os,
                 client_voice):
        self.server_id = server_id
        self.validator = validator
        self.discord_account = discord_account
        self.connector = connector
        self.manager_folder = manager
        self.message = message
        self.client_voice = client_voice
        self.server_players = server_players
        self.asyncio = asyncio
        self.os = os
        self.factory = None
        pass

    def get_entity(self):
        pytube_instance = pytube
        try:
            self.factory = SoloTrackYoutubeFactory(pytube_instance, self.discord_account, self.validator)
            entity = self.factory.get_instance_track_solo()
        except:
            self.factory = PlaylistYoutubeFactory(pytube_instance, self.discord_account, self.validator)
            entity = self.factory.get_instance_playlist_youtube()
        return entity

    async def init_player(self):
        entity = self.get_entity()
        try:
            self.connector.get_voice_channel()
            self.client_voice = await self.connector.get_voice_client()
        except:
            pass

        if self.server_id not in self.server_players:
            self.server_players[self.server_id] = Player(self.client_voice, self.asyncio, pytube,
                                                         self.manager_folder,
                                                         discord,
                                                         self.os)
        player = self.server_players[self.server_id]

        # Adiciona a musica na queue dependendo da sua instancia
        player.queue.extend(entity.urls)

        return player
