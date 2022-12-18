import os
import sys
sys.path.insert(0, "src//")
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import pyqtSignal
from functional.book import Book
from gui.windows.detailsWindow import DetailWindow

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
            title.setText(book.getTitle()[:18]+ '...')

        
        if book.getPicture() == None:
            book.setPicture(os.path.join(os.path.abspath('src/assets/books/'), f"50ShadesOfGrey.jpg"))
        #print("TSTSSTTEEFTS" + book.getPicture())
        image = QImage(os.path.join(os.path.abspath('src/assets/books/'), f"{book.getPicture()}"))
        lable = PictureLabel(image,title, book.getID())
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

    imgParam = QLabel
    titleParam = QLabel
    clicked = pyqtSignal(int)

    def __init__(self, image, title, id, parent=None):
        super(PictureLabel, self).__init__(parent)
        self.imgParam = image
        self.titleParam = title
        cover = QPixmap(image)
        cover = cover.scaledToHeight(200)
        self.setPixmap(cover)

    def mousePressEvent(self, event):
        self.clicked.emit(id)
        #self.stats = DetailWindow(self.imgParam, self.titleParam)
        #self.stats.show()
