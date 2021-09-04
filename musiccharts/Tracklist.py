import os
from os.path import join

from musiccharts import AutoString
from musiccharts.Track import Track


class TracklistIterator(object):
    def __init__(self, tracklist):
        self.tracklist = tracklist.tracklist
        self.index = 0

    def __next__(self):
        if self.index >= len(self.tracklist):
            raise StopIteration
        result = self.tracklist[self.index]
        self.index += 1
        return result


class Tracklist(object):
    def __init__(self,
                 title: str = "UNTITLED",
                 description: str = "No description",
                 genre_or_category: str = "Uncategorized",
                 tracklist: list = None):
        self.title = title
        self.description = description
        if tracklist is None:
            tracklist = []
        self.tracklist = tracklist
        self.genre_or_category = genre_or_category

    def add(self, track: Track):
        self.tracklist.append(track)

    def delete(self, track: Track):
        if track not in self.tracklist:
            raise TrackNotInTrackListError(track)
        self.tracklist.remove(track)

    def clear(self):
        self.tracklist.clear()

    def prettify(self) -> str:
        pretty_string = f'Tracklist: {self.title}\n' \
                        f'Description: {self.description}\n' \
                        f'Title(s): {len(self.tracklist)}\n\n'
        for track in self:
            pretty_string += f'{track.prettify()}\n'
        return pretty_string

    def table(self, show_metadata: bool = False) -> str:
        return self.separate('\t', show_metadata)

    def semicolon_separated(self, show_metadata: bool = False) -> str:
        return self.separate(';', show_metadata)

    def separate(self, separator: str = '\t', show_metadata: bool = False) -> str:
        if separator != '\t':
            if separator in self.separate('\t'):
                raise ForbiddenSeparatorError(separator, 'the separator is in the text to separate')

        head = ''
        if show_metadata:
            head += f'Tracklist{separator}{self.title}\n' \
                    f'Description{separator}{self.description}\n' \
                    f'Title(s){separator}{len(self.tracklist)}\n\n'

        head += f'Title{separator}' \
                f'Remix{separator}' \
                f'Artists{separator}' \
                f'Remixers{separator}' \
                f'Label{separator}' \
                f'Genre{separator}' \
                f'Release Date\n'

        content = ''
        for track in self:
            title = track.title
            remix = track.remix
            artists = ', '.join(str(artist) for artist in track.artists)
            remixers = ', '.join(str(remixer) for remixer in track.remixers)
            label = track.label
            genre = track.genre
            release_date = track.release_date.date()

            content += f'{title}{separator}' \
                       f'{remix}{separator}' \
                       f'{artists}{separator}' \
                       f'{remixers}{separator}' \
                       f'{label}{separator}' \
                       f'{genre}{separator}' \
                       f'{release_date}\n'

        full_info = f'{head}{content}'
        return full_info

    def to_csv_file(self, file_name: str = None, directory: str = None,
                    separator: str = ';', show_metadata: bool = False):
        if file_name is None:
            file_name = f"{self.title}.csv"

        file_name = file_name.replace(' /', ',')
        file_name = file_name.replace('/', ', ')

        if directory is None:
            directory = os.path.expanduser("~")

            if not os.path.isdir(join(directory, "MusicCharts")):
                os.mkdir(join(directory, "MusicCharts"))
            directory = join(directory, "MusicCharts")

            if "top100" in self.title.replace(" ", "").lower():
                if not os.path.isdir(join(directory, "Top 100")):
                    os.mkdir(join(directory, "Top 100"))
                directory = join(directory, "Top 100")

            genre_or_category_formatted_temp = self.genre_or_category.replace(' /', ',').replace('/', ', ')
            if not os.path.isdir(join(directory, genre_or_category_formatted_temp)):
                os.mkdir(join(directory, genre_or_category_formatted_temp))
            directory = join(directory, genre_or_category_formatted_temp)

        file = open(join(directory, file_name), "w", encoding='utf-8')
        file.write(self.separate(separator, show_metadata))

    def __str__(self):
        return AutoString.auto_string(self)

    def __iter__(self):
        return TracklistIterator(self)


class TrackNotInTrackListError(Exception):
    def __init__(self, track: Track = None):
        if track.title is None:
            self.message = 'Track not in this tracklist'
        else:
            self.message = f'Track {track.title} not in this tracklist'
        super().__init__(self.message)


class ForbiddenSeparatorError(Exception):
    def __init__(self, separator: str = None, cause: str = None):
        if separator is None:
            self.message = 'The used separator is forbidden'
        else:
            self.message = f'The used separator ("{separator}") is forbidden'
        if cause is not None:
            self.message += f', because {cause}'
        super().__init__(self.message)
