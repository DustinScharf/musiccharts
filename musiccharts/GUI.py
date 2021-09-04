from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel, \
    QHBoxLayout, QGridLayout

from musiccharts.GenreButton import GenreButton
from musiccharts.MusicCharts import MusicCharts


class GUI(object):
    def get_all_charts(self):
        self.music_charts.all_top_100_to_csv()

    def __init__(self):
        self.music_charts = MusicCharts()

        app = QApplication([])
        window = QWidget()
        # window.setWindowIcon(QtGui.QIcon("icon.ico"))
        window.setWindowTitle("MusicCharts")
        window.setMinimumWidth(400)
        window.setMinimumWidth(300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("<b><center>Scrap top chart lists</center></b>"))

        layout.addWidget(QLabel("<hr>"))

        layout.addWidget(QLabel("<b>All genres</b>"))

        get_all_charts_button = QPushButton("ALL GENRES")
        layout.addWidget(get_all_charts_button)
        get_all_charts_button.clicked.connect(self.get_all_charts)

        layout.addWidget(QLabel("<br>"))

        layout.addWidget(QLabel("<b>Specific genre</b>"))

        genre_layout = QGridLayout()

        DRUM_AND_BASS_button = GenreButton(genre_layout, 1, "DRUM_AND_BASS", 0, 0)
        HARD_TECHNO_button = GenreButton(genre_layout, 2, "HARD_TECHNO", 0, 1)
        ELECTRONICA_button = GenreButton(genre_layout, 3, "ELECTRONICA", 0, 2)

        HOUSE_button = GenreButton(genre_layout, 5, "HOUSE", 1, 0)
        TECHNO_button = GenreButton(genre_layout, 6, "TECHNO", 1, 1)
        TRANCE_button = GenreButton(genre_layout, 7, "TRANCE", 1, 2)
        HARD_DANCE_AND_HARDCODE_button = GenreButton(genre_layout, 8, "HARD_DANCE_AND_HARDCODE", 2, 0)
        BREAKS_AND_BREAKBEAT_AND_UK_BASS_button = GenreButton(genre_layout, 9, "BREAKS_AND_BREAKBEAT_AND_UK_BASS", 2, 1)

        TECH_HOUSE_button = GenreButton(genre_layout, 11, "TECH_HOUSE", 2, 2)
        DEEP_HOUSE_button = GenreButton(genre_layout, 12, "DEEP_HOUSE", 3, 0)
        PSY_TRANCE_button = GenreButton(genre_layout, 13, "PSY_TRANCE", 3, 1)
        MINIMAL_AND_DEEP_TECH_button = GenreButton(genre_layout, 14, "MINIMAL_AND_DEEP_TECH", 3, 2)
        PROGRESSIVE_HOUSE_button = GenreButton(genre_layout, 15, "PROGRESSIVE_HOUSE", 4, 0)
        DJ_TOOLS_button = GenreButton(genre_layout, 16, "DJ_TOOLS", 4, 1)

        DUBSTEP_button = GenreButton(genre_layout, 18, "DUBSTEP", 4, 2)

        layout.addLayout(genre_layout)

        layout.addWidget(QLabel("<hr>"))

        layout.addWidget(QLabel("( The CSV files go into the directory <b>HOME/MusicCharts</b> )"))

        window.setLayout(layout)
        window.show()
        app.exec()
