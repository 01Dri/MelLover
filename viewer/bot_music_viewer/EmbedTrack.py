from constants.Constants import COLOR_FOR_EMBEDS, TITLE_EMBED_FOR_MUSIC


class EmbedTrack:

    def __init__(self, discord, name_music, length, author, author_image):
        self.discord = discord
        self.name_music = name_music
        self.length = length
        self.author = author
        self.author_image = author_image
        pass

    def get_embed_for_add_musics(self):
        embed = self.discord.Embed(title=TITLE_EMBED_FOR_MUSIC, color=COLOR_FOR_EMBEDS)
        embed.add_field(name="Música adicionada: ", value=f'{self.name_music}', inline=True)
        embed.set_footer(text=f'Pedida por {self.author}', icon_url=self.author_image)
        return embed

    def get_embed_for_current_track(self):
        embed = self.discord.Embed(title="Mel Musicas", color=COLOR_FOR_EMBEDS)
        embed.add_field(name="Música atual: ", value=f"{self.name_music}", inline=False)
        embed.set_footer(text=f'Pedida por {self.author}', icon_url=self.author_image)
        return embed


