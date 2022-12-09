import json
import os
import requests
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QWidget, QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QSize, Qt

from GUI.helper.downloadImg import BookViewFunktions


class LibraryView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')

        self.bookView = BookView()
        self.booksFilter = BooksFilter()

        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.booksFilter)
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)


class BooksFilter(QFrame):

    def __init__(self):
        super(QFrame, self).__init__()
        self.setMaximumWidth(150)

        self.genreBtn = self.addFilterBtn('Genre')
        self.recommendedBtn = self.addFilterBtn('Recomended')
        self.recentlyAddedBtn = self.addFilterBtn('Recently added')

        self.horiLayout = QVBoxLayout()
        self.horiLayout.addStretch()
        self.horiLayout.addWidget(self.genreBtn)
        self.horiLayout.addWidget(self.recommendedBtn)
        self.horiLayout.addWidget(self.recentlyAddedBtn)
        self.horiLayout.addStretch()

        self.setLayout(self.horiLayout)

    def addFilterBtn(self, buttonText):
        btn = QPushButton()
        btn.setFixedHeight(40)
        btn.setObjectName('filterBtn')
        btn.setText(buttonText)
        return btn


class BookView(QFrame, BookViewFunktions):

    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')

        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMaximumHeight(300)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        data = None
        with open(os.path.abspath("src/assets/books/books.json")) as json_file:
            data = json.load(json_file)

        self.loadBooks(data[:5])

        self.container.setLayout(self.containerHoriLayout)

        layout = QHBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)
        self.loadBooks(data[:5])
