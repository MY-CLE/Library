import json
import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QWidget,QLabel )
from PyQt6.QtCore import Qt
from gui.elements.guibook import GuiBook
from gui.helper.loadImgDB import Bookloader
class BorrowedView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView()
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)
        
class BookView(QFrame):
    borrowedBooksViewCount = 0
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMaximumHeight(300)
        self.bookLoader = Bookloader()
        self.bookLoader.bookloaded.connect(self.bookRecived)
        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        
        self.boxDescription = QLabel()
        self.boxDescription.setObjectName('boxDescription')
        self.boxDescription.setText('No User logged in')  
        
        self.loadBooks(4)
        
        self.containerVertLayout = QVBoxLayout()
        self.containerVertLayout.addWidget(self.boxDescription)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)
        
        
        
        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        self.setLayout(horilayout)
        
    def updateUser(self, id):
        self.boxDescription.setText(f'Your Borrowed Books, {id}')
        
    def loadBooks(self, amount =6):
        #print('loadbooks in Libview')
        for i in range(1,amount):
            self.bookLoader.loadBook(i)
            
    def bookRecived(self, bookinfo):
        #print('recive books in Libview')
        book = GuiBook(bookinfo)
        #print(book.getId())
        self.containerHoriLayout.addWidget(book)
        
    
        