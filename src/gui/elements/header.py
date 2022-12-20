import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
class Header(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('header')
        self.setMaximumHeight(200)
        self.setFrameShape(QFrame.Shape.NoFrame)
        
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/logo/hse-library-logo-smaller-removebg.png'))
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
        """ vertLayout.addLayout(containerLayout) """
        vertLayout.addLayout(logoLayout)
        vertLayout.addWidget(searchTextInput)
        self.setLayout(vertLayout)