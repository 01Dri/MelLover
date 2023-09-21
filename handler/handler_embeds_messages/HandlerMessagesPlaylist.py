from viewer.bot_music_viewer.EmbedPlaylist import EmbedPlaylist


class HandlerMessagePlaylist:

    def __init__(self, discord, playlist, discord_account):
        self.discord = discord
        self.playlist = playlist
        self.discord_account = discord_account
        pass

    def send_message_for_add_playlist(self):
        embed = EmbedPlaylist(self.discord, self.playlist.name, self.playlist.description, self.playlist.length,
                              self.discord_account.name, self.discord_account.avatar_url)

        return embed.get_embed_for_add_playlist()

    def send_message_for_current_track_for_playlist(self):
        embed = EmbedPlaylist(self.discord, self.playlist.name, self.playlist.description, self.playlist.length,
                              self.discord_account.name, self.discord_account.avatar_url)

        return embed.get_embed_for_add_playlist()
