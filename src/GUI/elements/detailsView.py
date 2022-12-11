import json
import os
from PyQt6.QtWidgets import (
    QHBoxLayout, QLayout, QVBoxLayout, QFrame, QWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage


class DetailsView(QFrame):
    def __init__(self, img, title):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView(img, title)
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)


class BookView(QFrame):
    def __init__(self, img, title):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMaximumWidth(300)
        self.container.setMaximumHeight(300)

        self.textContainer = QWidget()
        self.textContainer.setObjectName("bookViewContainer")
        self.textContainer.setMinimumWidth(200)
        self.textContainer.setMaximumHeight(300)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.textContainerHoriLayout = QHBoxLayout()
        self.textContainerHoriLayout.setAlignment(
            Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel()
        cover = QPixmap(img)
        cover = cover.scaledToHeight(290)
        cover = cover.scaledToWidth(200)
        self.label.setPixmap(cover)

        self.title = QLabel()
        self.title = title

        bookData = None
        with open(os.path.abspath("src/assets/books/books.json")) as json_file:
            bookData = json.load(json_file)

        self.bookDesc = QLabel
        self.bookAuth = QLabel
        self.bookDate = QLabel

        # alle Daten eines Buchs anzeigen, Hashmap(titel,Book-Object)?

        self.textContainerVertLayout = QVBoxLayout()
        # self.textContainerVertLayout.addWidget(self.bookAuth)
        self.textContainerVertLayout.addLayout(self.textContainerHoriLayout)
        self.textContainer.setLayout(self.textContainerVertLayout)

        self.containerVertLayout = QVBoxLayout()
        self.containerHoriLayout.addWidget(self.label)

        self.containerVertLayout.addWidget(self.title)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)

        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        horilayout.addWidget(self.textContainer)
        self.setLayout(horilayout)
