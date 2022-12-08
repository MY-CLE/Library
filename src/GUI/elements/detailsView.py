import json
import os
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame, QWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage


class DetailsView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView()
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)


class BookView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(200)
        self.container.setMinimumHeight(300)

        self.textContainer = QWidget()
        self.textContainer.setObjectName("bookViewContainer")
        self.textContainer.setMinimumWidth(200)
        self.textContainer.setMaximumHeight(200)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        data = None
        with open(os.path.abspath("src/assets/books/books.json")) as json_file:
            data = json.load(json_file)

        # self.loadBooks(data[:3])

        #cover = QPixmap()

        #self.author = QLabel()
        #self.pages = QLabel()
        self.title = QLabel()

        # self.title.setObjectName('details')
        #self.title = title

        #self.boxDescription = QLabel()
        # self.boxDescription.setObjectName('boxDescription')
        #self.boxDescription.setText('No User logged in')

        self.containerVertLayout = QVBoxLayout()
        self.containerVertLayout.addWidget(self.title)
        # self.containerVertLayout.addWidget(self.author)
        # self.containerVertLayout.addWidget(self.pages)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.textContainer.setLayout(self.containerVertLayout)

        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        horilayout.addWidget(self.textContainer)
        self.setLayout(horilayout)
