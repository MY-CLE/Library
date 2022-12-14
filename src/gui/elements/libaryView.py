import sys

from gui.elements.bookView import BookView, BooksFilter
sys.path.insert(0, "src//")
from PyQt6.QtWidgets import (
    QHBoxLayout, QFrame)
class LibraryView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')

        self.bookView = BookView(5)
        self.booksFilter = BooksFilter()

        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.booksFilter)
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)