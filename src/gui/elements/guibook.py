import os
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import pyqtSignal
from functional.book import Book

from GUI.windows.detailsWindow import DetailWindow


class GuiBook(QWidget):
    sendClicked = pyqtSignal(int)

    def __init__(self, book: Book):
        super(QWidget, self).__init__()
        self.id = book.getID()
        title = QLabel()
        title.setObjectName('bookTitleLable')

        if len(book.getTitle()) <= 20:
            title.setText(book.getTitle())
        else:
            title.setText(book.getTitle()[:18] + '...')

        if not book.getPicture():
            book.setPicture('50_shades_of_grey.jpg')
        imgpath = os.path.join(os.path.abspath(
            'src/assets/books/'), book.getPicture())
        image = QImage(imgpath)
        lable = PictureLabel(image, book)
        lable.clicked.connect(self.bookClicked)
        lable.setObjectName('bookCoveLable')

        bookLayout = QVBoxLayout()
        bookLayout.addStretch()
        bookLayout.addWidget(lable)
        bookLayout.addWidget(title)
        bookLayout.addStretch()
        self.setLayout(bookLayout)

    def bookClicked(self, id):
        print(f'bookclicked : {id}')
        self.sendClicked.emit(id)

    def getId(self):
        return self.id


class PictureLabel(QLabel):

    clicked = pyqtSignal(int)

    def __init__(self, image, book: Book, parent=None):
        super(PictureLabel, self).__init__(parent)
        self.bookID = book.getID()
        cover = QPixmap(image)
        cover = cover.scaledToHeight(200)
        self.setPixmap(cover)

    def mousePressEvent(self, event):
        self.clicked.emit(self.bookID)
        #self.stats = DetailWindow(self.imgParam, self.titleParam)
        # self.stats.show()
