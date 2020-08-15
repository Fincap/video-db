import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from db import DatabaseController
from model import Manager


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # selected_database = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a file to open",
        #                                                           filter="Video Database files (*.vdb)")[0]

        # INITIALIZE MODEL #

        selected_database = "data/tables.vdb"
        connection = sqlite3.connect(selected_database)
        db_controller = DatabaseController(connection)

        self.manager = Manager(db_controller)

        # CONSTRUCT INTERFACE #

        self.setWindowTitle("Video Database")
        self.setMinimumSize(800, 500)

        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()

        self.videos_list = QtWidgets.QListWidget()
        self.videos_list.itemDoubleClicked.connect(self.list_item_double_clicked)
        self.init_list_model()
        self.main_layout.addWidget(self.videos_list)

        options_pane = OptionsPane()
        self.main_layout.addWidget(options_pane)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def init_list_model(self):
        for video in self.manager.get_all_videos():
            self.videos_list.addItem(video)

    def list_item_double_clicked(self, item):
        print(item)


class OptionsPane(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setMinimumWidth(250)
        self.layout = QtWidgets.QVBoxLayout()

        example_text = QtWidgets.QLabel("Example text")
        self.layout.addWidget(example_text)

        example_button = QtWidgets.QPushButton("Example button")
        self.layout.addWidget(example_button)

        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
