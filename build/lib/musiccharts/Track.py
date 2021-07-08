from datetime import date

from musiccharts import AutoString


class Track(object):
    def __init__(self,
                 title: str = "NO TRACK TITLE SET!",
                 remix: str = None,
                 artists: list = None,
                 remixers: list = None,
                 label: str = None,
                 genre: str = None,
                 release_date: date = None):
        self.title = title
        self.remix = remix
        self.artists = artists
        self.remixers = remixers
        self.label = label
        self.genre = genre
        self.release_date = release_date

    def prettify(self) -> str:
        artists = f'{", ".join(str(artist) for artist in self.artists)}'
        title = self.title
        remix_info = f'{f"({self.remix})" if "Original" not in self.remix else ""}'

        pretty_string = f'{artists} - {title} {remix_info}'

        return pretty_string

    def __str__(self):
        return AutoString.auto_string(self)
