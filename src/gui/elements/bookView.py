from GUI.helper.loadImgDB import Bookloader
from GUI.elements.guibook import GuiBook
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QPushButton)
import sys
sys.path.insert(0, "src//")


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
    bookclickedBookView = pyqtSignal(int)

    def __init__(self, ids, filter=True):
        self.bookCount = 0
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.bookLoader = Bookloader()
        self.bookLoader.bookloaded.connect(self.bookRecived)
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMinimumHeight(400)

        self.containerGridLayout = QGridLayout()
        self.containerGridLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.container.setLayout(self.containerGridLayout)

        if type(ids) is int:
            ids = range(1, 13)

        self.loadBooks(ids)

        layout = QVBoxLayout()
        if filter:
            bookfilter = BooksFilter()
            layout.addWidget(bookfilter)
        layout.addWidget(self.container)
        self.setLayout(layout)

    def loadBooks(self, ids: list):
        print('loadbooks in Libview')
        for id in ids:
            self.bookLoader.loadBook(id)

    def bookRecived(self, bookinfo):
        #print('recive books in Libview')
        self.book = GuiBook(bookinfo)
        self.book.sendClicked.connect(self.sendClickedBookview)
        self.bookCount = self.containerGridLayout.count()
        print(int(self.bookCount/6), self.bookCount % 6)
        self.containerGridLayout.addWidget(
            self.book, int(self.bookCount/6), self.bookCount % 6)

    def sendClickedBookview(self, bookNo):
        self.bookclickedBookView.emit(bookNo)
