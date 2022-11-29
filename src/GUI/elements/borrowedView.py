import json
import os
import requests
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QSize, Qt
class BorrowedView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        
        self.bookView = BookView()
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)
        
class BookView(QFrame):
    
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
        
        for count, book in enumerate(data):
            print(book["img-src"])
            if count< 3:
                self.addBook(book)
               
        self.containerHoriLayout.addStretch()
               
        boxDescription = QLabel()
        boxDescription.setObjectName('boxDescription')
        boxDescription.setText('Your Borrowes Books:')  
        
        
        self.containerVertLayout = QVBoxLayout()
        self.containerVertLayout.addWidget(boxDescription)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)
        
        
        
        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        self.setLayout(horilayout)
        
    def addBook(self, book):
        
        self.book = QWidget()
        
        self.title = QLabel()
        self.title.setObjectName('bookTitleLable')
        
        if len(book['title']) <= 20: 
            self.title.setText(book['title'])
        else:
            self.title.setText(book['title'][:18] + '...')
        self.lable = QLabel()
        self.lable.setObjectName('bookCoveLable')
        image = QImage()
        image.loadFromData(requests.get(book['img-src']).content)
        cover = QPixmap(image)
        cover = cover.scaledToHeight(200)
        self.lable.setPixmap(cover)
        
        bookLayout = QVBoxLayout()
        bookLayout.addStretch()
        bookLayout.addWidget(self.lable)
        bookLayout.addWidget(self.title)
        bookLayout.addStretch()
        self.book.setLayout(bookLayout)
        
        self.containerHoriLayout.addWidget(self.book)