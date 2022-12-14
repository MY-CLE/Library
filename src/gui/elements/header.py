import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap, QIcon
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
        container.setFixedSize(100,100)

        containerLayout = QHBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.profileBtn = QPushButton()
        self.profileBtn.setObjectName('profilBtn')
        self.profilIcon = QIcon('src/assets/icon/logout.png')
        self.profileBtn.setIcon(self.profilIcon)
        #self.profileBtn.iconSize(QSize(50,50))
        
        self.homeBtn = QPushButton()
        self.homeBtn.setObjectName('homeBtn')
        self.homeIcon = QIcon('src/assets/icon/home.png')
        self.homeBtn.setIcon(self.homeIcon)
        #self.homeBtn.iconSize(QSize(50,50))
        
        containerLayout.addWidget(self.profileBtn)
        containerLayout.addWidget(self.homeBtn)        
        container.setLayout(containerLayout)
        
        layout = QHBoxLayout()
        layout.addWidget(container)
        self.setLayout(layout)