from constants.Constants import COLOR_FOR_EMBEDS, TITLE_EMBED_FOR_MUSIC


class EmbedPlaylist:

    def __init__(self, discord, name_playlist, description, amount_musics, author, author_image):
        self.discord = discord
        self.name_playlist = name_playlist
        self.description = description
        self.amount_musics = amount_musics
        self.author = author
        self.author_image = author_image
        pass

    def get_embed_for_add_playlist(self):
        embed = self.discord.Embed(title=TITLE_EMBED_FOR_MUSIC, color=COLOR_FOR_EMBEDS)
        embed.add_field(name=f"Playlist", value=f"{self.name_playlist.upper()}")
        embed.add_field(name=f"Descrição: ", value=f"{self.description}", inline=False)
        embed.add_field(name=f"Músicas: ", value=f"{self.amount_musics} músicas carregadas", inline=False)
        embed.set_footer(text=f'Pedida por {self.author}', icon_url=self.author_image)
        return embed



