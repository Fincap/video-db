import sqlite3

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

from db import DatabaseController
from model import Manager
from videos import Video
from view.popups import AddVideoWindow


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

        self.init_actions()

        # Set main layout
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()

        # Create create left panel
        self.left_panel = QtWidgets.QWidget()
        self.left_panel_layout = QtWidgets.QVBoxLayout()

        # Create filter textbox
        self.filter_textbox = QtWidgets.QLineEdit()
        self.left_panel_layout.addWidget(self.filter_textbox)

        # Create video list
        self.videos_list = QtWidgets.QListWidget()
        self.refresh_videos_list()
        self.left_panel_layout.addWidget(self.videos_list)

        self.left_panel.setLayout(self.left_panel_layout)
        self.main_layout.addWidget(self.left_panel)

        # Create right panel
        self.options_pane = OptionsPane(self)
        self.main_layout.addWidget(self.options_pane)

        # Connect signals
        self.videos_list.itemClicked.connect(self.options_pane.refresh_info)
        self.videos_list.itemDoubleClicked.connect(self.list_item_double_clicked)

        # Finalize layout
        self.toolbar = Toolbar(self)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def init_actions(self):
        self.action_new_video = QtWidgets.QAction(QtGui.QIcon('res/add_icon.png'), "New Video", self)
        self.action_new_video.triggered.connect(self.add_new_video)

        # self.action_exit = QtWidgets.QAction("Exit", self)
        # self.action_exit.triggered.connect(QtCore.QCoreApplication.exit)

    def refresh_videos_list(self):
        self.videos_list.clear()
        for video in self.manager.get_all_videos():
            self.videos_list.addItem(video)

    def list_item_double_clicked(self, video: Video):
        # Opens URL of video object
        url = QtCore.QUrl(video.url)
        if not QtGui.QDesktopServices.openUrl(url):
            QtWidgets.QMessageBox.warning(self, 'Open URL', 'Could not open URL. Ensure it is formatted correctly.')

    def add_new_video(self):
        # Show add new video window
        show_window = AddVideoWindow(self.manager)
        show_window.exec_()

    def add_tag(self, tag_item: QtWidgets.QListWidgetItem):
        pass

    def delete_tag(self, tag_item: QtWidgets.QListWidgetItem):
        pass


class OptionsPane(QtWidgets.QWidget):

    def __init__(self, main_window):
        QtWidgets.QWidget.__init__(self)

        self.main_window = main_window
        self.selected_video = None

        self.setMinimumWidth(250)
        self.layout = QtWidgets.QVBoxLayout()

        self.label_url = QtWidgets.QLabel("URL")
        self.textbox_url = QtWidgets.QLineEdit()
        self.textbox_url.setDisabled(True)

        self.label_title = QtWidgets.QLabel("Title")
        self.textbox_title = QtWidgets.QLineEdit()
        self.textbox_title.setDisabled(True)

        self.label_tags = QtWidgets.QLabel("Tags (separated by commas)")
        self.list_tags = QtWidgets.QListWidget()

        self.tag_buttons_widget = QtWidgets.QWidget()
        self.tag_buttons_layout = QtWidgets.QHBoxLayout()

        self.button_add_tag = QtWidgets.QPushButton("Add Tag")
        self.tag_buttons_layout.addWidget(self.button_add_tag)

        self.button_remove_tag = QtWidgets.QPushButton("Delete Tag")
        self.tag_buttons_layout.addWidget(self.button_remove_tag)

        self.tag_buttons_widget.setLayout(self.tag_buttons_layout)

        self.layout.addWidget(self.label_url)
        self.layout.addWidget(self.textbox_url)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.textbox_title)
        self.layout.addWidget(self.label_tags)
        self.layout.addWidget(self.list_tags)
        self.layout.addWidget(self.tag_buttons_widget)

        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def refresh_info(self, new_selection: Video):
        self.selected_video = new_selection

        self.textbox_url.setText(new_selection.url)
        self.textbox_title.setText(new_selection.title)
        self.list_tags.clear()
        self.list_tags.addItems(new_selection.tags)


class Toolbar:

    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

        self.main_window.toolbar = self.main_window.addToolBar("Actions")
        self.main_window.toolbar.setMovable(False)

        self.main_window.toolbar.addAction(self.main_window.action_new_video)
        #self.main_window.toolbar.addAction(self.main_window.action_exit)
