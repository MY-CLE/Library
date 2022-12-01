import sys
import json
import os
import requests
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit, )
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, QThreadPool
from gui.helper.downloadImg import BookViewFunktions
class BorrowedView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        
        self.bookView = BookView()
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)
        
class BookView(QFrame, BookViewFunktions):
    borrowedBooksViewCount = 0
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
        
        self.loadBooks(data[:3])
               
        boxDescription = QLabel()
        boxDescription.setObjectName('boxDescription')
        boxDescription.setText('Your Borrowed Books:')  
        
        
        self.containerVertLayout = QVBoxLayout()
        self.containerVertLayout.addWidget(boxDescription)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)
        
        
        
        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        self.setLayout(horilayout)