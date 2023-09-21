from viewer.bot_music_viewer.EmbedTrack import EmbedTrack


class HandlerMessagesSoloTrack:

    def __init__(self, discord, track, discord_account):
        self.discord = discord
        self.track = track
        self.discord_account = discord_account
        pass

    def send_message_for_track_add(self):
        embed = EmbedTrack(self.discord, self.track.name, self.track.time, self.discord_account.name,
                           self.discord_account.avatar_url)
        return embed.get_embed_for_add_musics()

    def send_message_for_current_track(self):
        embed = EmbedTrack(self.discord, self.track.name, self.track.time, self.discord_account.name,
                           self.discord_account.avatar_url)
        return embed.get_embed_for_current_track()


