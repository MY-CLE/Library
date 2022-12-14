import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
class CustHeader(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('header')
        self.setMaximumHeight(200)
        
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/Logo/hse-library-logo-smaller-removebg-preview.png'))
        logo = logo.scaledToHeight(65)
        logoLable.setPixmap(logo)
        
        searchTextInput = QLineEdit()
        searchTextInput.setPlaceholderText("Search")
        searchTextInput.setObjectName("searchTextInput")
        #searchTextInput.setMaximumWidth()
        searchTextInput.setMinimumHeight(65)
        searchTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.iconbar = IconBar()
        
        horiLayout = QHBoxLayout()
        horiLayout.addWidget(logoLable)
        horiLayout.addWidget(searchTextInput)
        horiLayout.addWidget(self.iconbar)
        self.setLayout(horiLayout)
        
        
class IconBar(QFrame):
    
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('iconBar')
        
        container = QWidget()
        container.setObjectName("iconBarContainer")
        container.setFixedSize(100,65)

        containerLayout = QHBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.profileBtn = QPushButton()
        self.homeBtn = QPushButton()
        containerLayout.addWidget(self.profileBtn)
        containerLayout.addWidget(self.homeBtn)        
        container.setLayout(containerLayout)
        
        layout = QHBoxLayout()
        layout.addWidget(container)
        self.setLayout(layout)