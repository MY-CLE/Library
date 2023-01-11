from gui.helper.loadImgDB import Bookloader
from gui.elements.guibook import GuiBook
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from functional.book import Book
from PyQt6.QtWidgets import (
    QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QPushButton, QScrollArea)
import sys
sys.path.insert(0, "src//")

import asyncio


class BooksFilter(QFrame):

    def __init__(self):
        super(QFrame, self).__init__()
        self.setMaximumHeight(80)
        self.recentlyAddedBtn = QPushButton()
        self.recentlyAddedBtn.setText('Recently Added')
        self.recentlyAddedBtn.setObjectName('recentlyAddedBtn')
        self.recentlyAddedBtn.setContentsMargins(6, 2, 6, 2)
        self.recomendationsBtn = QPushButton()
        self.recomendationsBtn.setText('Recomendations')
        self.recomendationsBtn.setObjectName('recomendationsBtn')
        self.genreBtn = QPushButton()
        self.genreBtn.setText('Genre')
        self.genreBtn.setObjectName('genreBtn')

        self.horiLayout = QHBoxLayout()
        self.horiLayout.addStretch()
        self.horiLayout.addWidget(self.recentlyAddedBtn)
        self.horiLayout.addStretch()
        self.horiLayout.addWidget(self.recomendationsBtn)
        self.horiLayout.addStretch()
        self.horiLayout.addWidget(self.genreBtn)
        self.horiLayout.addStretch()

        self.setLayout(self.horiLayout)


class BookView(QFrame):
    bookclickedBookView = pyqtSignal(Book)

    def __init__(self, ids, filter=True):
        self.bookCount = 0
        super(QFrame, self).__init__()
        if type(ids) is int:
            ids = range(1, 13)
        self.setObjectName('bookView')
        self.bookLoader = Bookloader()
        self.bookLoader.bookloaded.connect(self.bookRecived)
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMinimumHeight(400)

        self.bookGridLayout = QGridLayout()
        self.bookGridLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        books = QWidget()
        books.setLayout(self.bookGridLayout)
        
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet('background: white; border: 0px')
        self.scroll.setWidget(books)
        
        containerLayout = QHBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        containerLayout.addWidget(self.scroll)
        self.container.setLayout(containerLayout)
        layout = QVBoxLayout()
        if filter:
            bookfilter = BooksFilter()
            layout.addWidget(bookfilter)
            
        layout.addWidget(self.container)
        self.setLayout(layout)
        self.loadBooks(ids)

    def loadBooks(self, ids: list):
        print('loadbooks in Libview')
        for id in ids:
            self.bookLoader.loadBook(id)

    def bookRecived(self, book):
        self.book = GuiBook(book)
        self.book.sendClicked.connect(self.sendClickedBookview)
        self.bookCount = self.bookGridLayout.count()
        print(int(self.bookCount/5), self.bookCount % 5)
        self.bookGridLayout.addWidget(self.book, int(self.bookCount/5), self.bookCount % 5)

    def sendClickedBookview(self, book: Book):
        self.bookclickedBookView.emit(book)
