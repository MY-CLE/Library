import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QWidget,QLabel, QPushButton, QSpacerItem)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class UserDetailsHeader(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('userDetailsHeader')
        self.setMinimumHeight(100)
        self.setFrameShape(QFrame.Shape.NoFrame)

        title = QLabel()
        title.setText('ACCOUNT')
        title.setObjectName('userDetailsTitle')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/logo/hse-library-logo-smaller-removebg.png'))
        logo = logo.scaledToHeight(100)
        logoLable.setPixmap(logo)        
        logoLable.setMinimumHeight(100)
        logoLable.setAlignment(Qt.AlignmentFlag.AlignBaseline)

     
        vertLayout = QVBoxLayout()
        vertLayout.addWidget(logoLable)
        vertLayout.addWidget(title)
        vertLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(vertLayout)