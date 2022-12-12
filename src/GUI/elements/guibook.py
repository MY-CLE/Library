import os
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import pyqtSignal

from gui.windows.detailsWindow import DetailWindow
class GuiBook(QWidget):
    sendClicked = pyqtSignal(int)
    def __init__(self, bookinfo):
        super(QWidget, self).__init__()
        self.id = bookinfo['bookid']; 
        title = QLabel()
        title.setObjectName('bookTitleLable')

        if len(bookinfo['title']) <= 20:
            title.setText(bookinfo['title'])
        else:
            title.setText(bookinfo['title'][:18] + '...')

        
        if bookinfo['picture'] == None:
            bookinfo['picture'] = os.path.join(os.path.abspath('src/assets/books/'), f"Image_{1}.jpg")
        image = QImage(bookinfo['picture'])
        lable = PictureLabel(image,title, bookinfo['bookid'])
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
