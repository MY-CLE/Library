import json
import os
import requests
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QSize, Qt
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
        btn= QPushButton()
        btn.setFixedHeight(40)
        btn.setObjectName('filterBtn')
        btn.setText(buttonText)
        return btn
        
        
        
        
class BookView(QFrame):
    
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMaximumHeight(300)

        self.containerLayout = QHBoxLayout()
        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        data = None
        with open(os.path.abspath("src/assets/books/books.json")) as json_file:
            data = json.load(json_file)
        
        for count, book in enumerate(data):
            print(book["img-src"])
            if count< 5:
                self.addBook(book)
        #for book in self.books:
        #    self.addBook(book)
               
        self.container.setLayout(self.containerLayout)
        
        layout = QHBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)
        
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
        
        self.containerLayout.addWidget(self.book)