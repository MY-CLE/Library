import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
class CustHeader(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('header')
        #self.setStyleSheet("background-color: yellow;")
        self.setMaximumHeight(200)
        
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/Logo/hse-library-logo-smaller.png'))
        logoLable.setPixmap(logo)
        
        searchTextInput = QLineEdit()
        searchTextInput.setPlaceholderText("Email")
        searchTextInput.setObjectName("searchTextInput")
        searchTextInput.setMaximumWidth(250)
        searchTextInput.setMinimumHeight(40)
        searchTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        
        
        
        
        horiLayout = QHBoxLayout()
        horiLayout.addWidget(logoLable)
        horiLayout.addWidget(searchTextInput)
        self.setLayout(horiLayout)
        
        
class Iconbar(QFrame):
    container = QWidget()
    container.setObjectName("loginContainer")
    container.setFixedSize(400,300)
    container.setStyleSheet('background-color: white')

    
    
    
    containerLayout = QHBoxLayout()
    containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    
    containerLayout.addWidget()
    containerLayout.addWidget()        
    container.setLayout(containerLayout)