import os
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import pyqtSignal
from functional.book import Book

from gui.windows.detailsWindow import DetailWindow
class GuiBook(QWidget):
    sendClicked = pyqtSignal(Book)
    def __init__(self, book: Book):
        super(QWidget, self).__init__()
        self.id = book.getID(); 
        title = QLabel()
        title.setObjectName('bookTitleLable')

        if len(book.getTitle()) <= 20:
            title.setText(book.getTitle())
        else:
            title.setText(book.getTitle()[:18] + '...')

        
        if book.getPicture()== None:
            book.setPicture= os.path.join(os.path.abspath('src/assets/books/'), f"50_shades_of_grey.jpg")
        image = QImage(book.getPicture())
        lable = PictureLabel(book)
        lable.clicked.connect(self.bookClicked)
        lable.setObjectName('bookCoveLable')

        bookLayout = QVBoxLayout()
        bookLayout.addStretch()
        bookLayout.addWidget(lable)
        bookLayout.addWidget(title)
        bookLayout.addStretch()
        self.setLayout(bookLayout)
    
    
    def bookClicked(self, book):
        print(f'bookclicked : {book.getID()}')
        self.sendClicked.emit(book)
        
    def getId(self):
        return self.id
        
        
class PictureLabel(QLabel):

    imgParam = QLabel
    titleParam = QLabel
    clicked = pyqtSignal(Book)

    def __init__(self, book, parent=None):
        self.book = book
        super(PictureLabel, self).__init__(parent)
        self.imgParam = book.getPicture()
        self.titleParam = book.getTitle()
        cover = QPixmap(book.getPicture())
        cover = cover.scaledToHeight(200)
        self.setPixmap(cover)

    def mousePressEvent(self, event):
        self.clicked.emit(self.book)
        #self.stats = DetailWindow(self.imgParam, self.titleParam)
        #self.stats.show()
