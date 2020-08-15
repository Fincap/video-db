from PyQt5 import QtWidgets, QtCore

from model.manager import Manager


class AddVideoWindow(QtWidgets.QDialog):

    def __init__(self, manager: Manager):
        QtWidgets.QDialog.__init__(self)
        self.manager = manager

        self.setWindowTitle("Add New Video")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.label_url = QtWidgets.QLabel("URL")
        self.textbox_url = QtWidgets.QLineEdit()

        self.label_title = QtWidgets.QLabel("Title")
        self.textbox_title = QtWidgets.QLineEdit()

        self.label_tags = QtWidgets.QLabel("Tags (separated by commas)")
        self.textbox_tags = QtWidgets.QLineEdit()

        self.add_button = QtWidgets.QPushButton("Add Video")
        self.add_button.clicked.connect(self.add_video)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_url)
        self.layout.addWidget(self.textbox_url)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.textbox_title)
        self.layout.addWidget(self.label_tags)
        self.layout.addWidget(self.textbox_tags)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

    def add_video(self):
        new_url = self.textbox_url.text()
        new_title = self.textbox_title.text()

        raw_tags = self.textbox_tags.text().split(',')
        new_tags = []
        for tag in raw_tags:
            new_tags.append(tag.strip())

        print(new_tags)

        self.manager.add_video(new_url, new_title, new_tags)
