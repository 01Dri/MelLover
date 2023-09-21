from constants.Constants import COLOR_FOR_EMBEDS, TITLE_EMBED_FOR_MUSIC, COLOR_FOR_EMBEDS_ERROR


class EmbedErros:

    def __init__(self, discord, message):
        self.discord = discord
        self.message = message
        pass

    def get_embed_error(self):
        embed = self.discord.Embed(title="Mel Musicas", color=COLOR_FOR_EMBEDS_ERROR)
        embed.add_field(name="ERRO: ", value=self.message, inline=False)
        return embed


