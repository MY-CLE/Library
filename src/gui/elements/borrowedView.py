from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QWidget,QLabel )
from PyQt6.QtCore import Qt
from gui.elements.guibook import GuiBook
from gui.helper.loadImgDB import Bookloader
class BorrowedView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView(3)
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addWidget(self.bookView)
        self.setLayout(mainHoriLayout)
    
        
    
        