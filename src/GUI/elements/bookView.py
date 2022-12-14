import sys
sys.path.insert(0, "src//")
from PyQt6.QtWidgets import (
    QHBoxLayout, QFrame, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton)
from PyQt6.QtCore import Qt, pyqtSignal
from gui.elements.guibook import GuiBook
from gui.helper.loadImgDB import Bookloader

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
        btn = QPushButton()
        btn.setFixedHeight(40)
        btn.setObjectName('filterBtn')
        btn.setText(buttonText)
        return btn


class BookView(QFrame):
    bookclickedBookView = pyqtSignal(int)
    def __init__(self, amount):
        self.userid = None
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.bookLoader = Bookloader()
        self.bookLoader.bookloaded.connect(self.bookRecived)
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMinimumWidth(500)
        self.container.setMaximumHeight(300)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.container.setLayout(self.containerHoriLayout)
        
        self.loadBooks(amount)
    
        layout = QHBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def loadBooks(self, amount =6):
        print('loadbooks in Libview')
        for i in range(1,amount):
            self.bookLoader.loadBook(i)
            
    def bookRecived(self, bookinfo):
        #print('recive books in Libview')
        self.book = GuiBook(bookinfo)
        self.book.sendClicked.connect(self.sendClickedBookview)
        self.containerHoriLayout.addWidget(self.book)
        
    def sendClickedBookview(self, bookNo):
        self.bookclickedBookView.emit(bookNo)
    
    def updateUser(self, id):
        self.userid = id