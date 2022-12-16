import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt
class Header(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('header')
        self.setMaximumHeight(200)
        self.setFrameShape(QFrame.Shape.NoFrame)
        
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/logo/hse-library-logo-smaller-removebg-preview.png'))
        logo = logo.scaledToHeight(100)
        logoLable.setPixmap(logo)        
        logoLable.setMinimumHeight(100)
        
        logoLayout = QHBoxLayout()
        logoLayout.addStretch()
        logoLayout.addWidget(logoLable)
        logoLayout.addStretch()
        
        searchTextInput = QLineEdit()
        searchTextInput.setPlaceholderText("Search")
        searchTextInput.setObjectName("searchTextInput")
        #searchTextInput.setMaximumWidth()
        searchTextInput.setMinimumHeight(65)
        searchTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        vertLayout = QVBoxLayout()
        vertLayout.addLayout(logoLayout)
        vertLayout.addWidget(searchTextInput)
        self.setLayout(vertLayout)