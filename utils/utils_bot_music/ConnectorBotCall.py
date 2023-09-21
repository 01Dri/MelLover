
from exception.AuthorIsNotConnectedInChannel import AuthorIsNotConnectedInChannel


class ConnectorBot:

    def __init__(self, ctx, discord):
        self.voice_channel = None
        self.ctx = ctx
        self.discord = discord

    def get_voice_channel(self):
        if self.ctx.author.voice is None or self.ctx.author.voice.channel is None:
            raise AuthorIsNotConnectedInChannel("O usuário precisa estar conectado em um canal de voz")

        self.voice_channel = self.ctx.author.voice.channel
        return self.voice_channel

    async def get_voice_client(self):
        if self.voice_channel is not None:
            return await self.voice_channel.connect()
        else:
            raise AuthorIsNotConnectedInChannel("O usuario precisa estar conectado em um chamada de voz!")



