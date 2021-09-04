from PyQt5.QtWidgets import QGridLayout, QPushButton

from musiccharts.MusicCharts import MusicCharts


class GenreButton(object):
    def __init__(self, genre_layout: QGridLayout, genre_id: int, genre: str, row:int, col:int):
        self.get_charts_button = QPushButton(genre)

        genre_layout.addWidget(self.get_charts_button,
                               row,
                               col)
        self.get_charts_button.clicked.connect(self.clicked)

        self.genre_id = genre_id

    def clicked(self):
        MusicCharts().top_100(self.genre_id).to_csv_file()
