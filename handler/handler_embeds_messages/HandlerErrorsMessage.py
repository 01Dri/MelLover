from viewer.bot_music_viewer.EmbedErrors import EmbedErros


class HandlerErrorsMessages:

    def __init__(self, discord, message):
        self.message = message
        self.discord = discord

    def send_message_error_emebed(self):
        embed = EmbedErros(self.discord,  self.message)
        return embed.get_embed_error()