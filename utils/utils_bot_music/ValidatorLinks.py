
from exception.UrlInvalidException import UrlInvalidException


class ValidatorUrls:

    def __init__(self, ctx):
        self.ctx = ctx

    def get_url_validated(self):
        try:
            parts = self.ctx.content.split()
        except:
            parts = self.ctx.split()
        if len(parts) < 2:
            raise UrlInvalidException("Nenhuma URL fornecida.")
        url_base = parts[1]
        url = parts[1].split("?")[0]

        if "https://www.youtube" in url or "https://youtu.be" in url or "https://youtube.com" in url:
            return self.validate_url_youtube(url_base)

        if "https://spotify.link" in url or "https://open.spotify.com" in url:
            return self.validate_url_spotify(url_base)

        raise UrlInvalidException(
            "A URL informada não é válida.")

    def validate_url_youtube(self, url):
        if not ("youtube.com" in url or "youtu.be" in url):
            raise UrlInvalidException(
                "A URL do YouTube informada não é válida. Deve conter 'youtube.com' ou 'youtu.be'.")
        return url

    def validate_url_spotify(self, url):
        if not ("spotify.link/" in url or "open.spotify.com/intl-pt/track" in url):
            raise UrlInvalidException(
                "A URL do Spotify informada não é válida. Deve conter 'spotify.link/' ou 'open.spotify.com/intl-pt/track'.")
        return url


