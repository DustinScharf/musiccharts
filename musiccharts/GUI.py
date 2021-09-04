from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel, \
    QHBoxLayout, QGridLayout

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

        get_techno_charts_button = QPushButton("Techno")
        genre_layout.addWidget(get_techno_charts_button, 2, 2)
        genre_layout.addWidget(get_techno_charts_button, 5, 5)
        # get_techno_charts_button.clicked.connect(self.get_all_charts)

        layout.addLayout(genre_layout)

        layout.addWidget(QLabel("<hr>"))

        layout.addWidget(QLabel("( The CSV files go into the directory <b>HOME/MusicCharts</b> )"))

        window.setLayout(layout)
        window.show()
        app.exec()
