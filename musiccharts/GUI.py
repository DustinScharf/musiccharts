from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel, QHBoxLayout


class GUI(object):
    def __init__(self):
        app = QApplication([])
        window = QWidget()
        # window.setWindowIcon(QtGui.QIcon("icon.ico"))
        window.setWindowTitle("MusicCharts")
        window.setMinimumWidth(400)
        window.setMinimumWidth(300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Hello"))

        window.setLayout(layout)
        window.show()
        app.exec()
