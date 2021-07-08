from datetime import datetime

import requests
from bs4 import BeautifulSoup

from musiccharts import genres, AutoString
from musiccharts.Track import Track
from musiccharts.Tracklist import Tracklist


class MusicCharts(object):
    def __init__(self):
        self.music_chart_source = 'https://www.beatport.com'
        self.genre_id = 1

    def top_100(self, genre_id: int = None, title: str = None) -> Tracklist:
        if genre_id is None:
            genre_id = self.genre_id

        if genre_id not in genres.ALL_GENRES:
            raise GenreNotExistsError(genre_id)

        self.genre_id = genre_id

        chart_site = requests.get(f'{self.music_chart_source}/genre/drum-bass/{genre_id}/top-100')
        chart_site_soup = BeautifulSoup(chart_site.text, 'html.parser')

        top_100_title_metadata = chart_site_soup.find('div', {'class': 'bp-top-ten-title'})
        top_100_genre = top_100_title_metadata.find('h5').text
        if title is None:
            title = f'Top 100 - {top_100_genre} ({datetime.today().date()})'
        pretty_today_date_string = datetime.today().date()
        description = f'This tracklist contains the Top 100 {top_100_genre} Tracks of {pretty_today_date_string}.'
        top_100 = Tracklist(title, description)

        chart_table_full = chart_site_soup.find('div', {'class': 'bucket tracks top-hundred-tracks'})
        chart_table_content = chart_table_full.find('ul', {'class': 'bucket-items ec-bucket'})

        for chart_table_entry in chart_table_content.find_all('li', {'class': 'bucket-item ec-item track'}):
            track_metadata = chart_table_entry.find('div', {'class': 'buk-track-meta-parent'})

            track_title_metadata = track_metadata.find('p', {'class': 'buk-track-title'})
            track_title = track_title_metadata.find('span', {'class': 'buk-track-primary-title'}).text
            track_remix = track_title_metadata.find('span', {'class': 'buk-track-remixed'}).text

            track_artists_metadata = track_metadata.find('p', {'class': 'buk-track-artists'})
            track_artists = []
            for track_artist_metadata in track_artists_metadata.find_all('a'):
                track_artists.append(track_artist_metadata.text)

            track_remixers_metadata = track_metadata.find('p', {'class': 'buk-track-remixers'})
            track_remixers = []
            for track_remixers_metadata in track_remixers_metadata.find_all('a'):
                track_remixers.append(track_remixers_metadata.text)

            track_label_metadata = track_metadata.find('p', {'class': 'buk-track-labels'})
            track_label = track_label_metadata.find('a').text

            track_genre_metadata = track_metadata.find('p', {'class': 'buk-track-genre'})
            track_genre = track_genre_metadata.find('a').text

            track_release_date_string = track_metadata.find('p', {'class': 'buk-track-released'}).text
            track_release_date = datetime.strptime(track_release_date_string, '%Y-%m-%d')

            track = Track(track_title,
                          track_remix,
                          track_artists,
                          track_remixers,
                          track_label,
                          track_genre,
                          track_release_date)

            top_100.add(track)

        if len(top_100.tracklist) > 0:
            top_100.genre_or_category = top_100.tracklist[0].genre

        return top_100

    def all_top_100_to_csv(self):
        process = 0
        finish = len(genres.ALL_GENRES)
        for genre_id in genres.ALL_GENRES:
            self.top_100(genre_id).to_csv_file()
            process += 1
            if process == finish:
                process_info_end = "\n"
            else:
                process_info_end = " | "
            print(f"({process} / {finish})", end=process_info_end)
        print()

    def __str__(self):
        return AutoString.auto_string(self)


class GenreNotExistsError(Exception):
    def __init__(self, genre_id: int = None):
        if genre_id is None:
            self.message = 'The requested genre_id does not exist'
        else:
            self.message = f'The requested genre_id {genre_id} does not exist'
        super().__init__(self.message)
