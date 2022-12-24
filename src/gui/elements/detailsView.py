from enum import Enum
import os
from PyQt6.QtWidgets import (
    QHBoxLayout, QLayout, QVBoxLayout, QFrame, QWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt,pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
from functional.account import Account
from functional.book import Book
from database.dbfunctions import checkisBorrowedTable, insertBorrowedTable, removeBorrowedTable

class BtnStatus(Enum):
    AVALABLE = 0
    UNAVALABLE = 1
    RETURN = 2
class DetailsView(QFrame):
    def __init__(self, book: Book, user: Account):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView(book, user)
        self.titleView = TitleView(book)
        mainVertLayout = QVBoxLayout()
        HoriLayout = QHBoxLayout()
        HoriLayout.addWidget(self.bookView)
        mainVertLayout.addWidget(self.titleView)
        mainVertLayout.addWidget(self.bookView)
        self.setLayout(mainVertLayout)


class TitleView(QFrame):
    def __init__(self, book: Book):
        super(QFrame, self).__init__()
        title = QLabel()
        title.setText(book.title)
        title.setObjectName('titleView')

        HoriLayout = QHBoxLayout()
        HoriLayout.addWidget(title)
        self.setLayout(HoriLayout)


class BookView(QFrame):
    borrowedBtnClicked = pyqtSignal(BtnStatus)
    def __init__(self, book: Book, user: Account):
        super(QFrame, self).__init__()
        self.book = book
        self.currentUser = user
        self.borrowedUserId = checkisBorrowedTable(self.book.id)
        self.setObjectName('bookView')
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMaximumWidth(300)
        self.container.setMaximumHeight(300)

        self.textContainer = QWidget()
        self.textContainer.setObjectName("bookViewTextContainer")
        self.textContainer.setMinimumWidth(300)
        self.textContainer.setMaximumHeight(300)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.textContainerHoriLayout = QHBoxLayout()
        # self.textContainerHoriLayout.setAlignment(
        # Qt.AlignmentFlag.AlignHCenter)

        bookTitle = QLabel()
        bookTitle.setText(book.title)

        bookAuthor = QLabel()
        bookAuthor.setText("Author: "+book.author)
        bookAuthor.setObjectName("details")

        imgpath = os.path.join(os.path.abspath('src/assets/books/'), book.picture)
        image = QImage(imgpath)
        bookCover = QPixmap(image)
        bookCover = bookCover.scaledToWidth(200)
        imageLabel = QLabel()
        imageLabel.setPixmap(bookCover)

        bookGenre = QLabel()
        bookGenre.setText("Genre: "+book.genre)
        bookGenre.setObjectName("details")

        bookRating = QLabel()
        bookRating.setText(f"Rating: {book.getAverageRating}")
        bookRating.setObjectName("details")

        bookisBorrowed = QLabel()
        bookisBorrowed.setText("Availability: Unavailable")
        bookisBorrowed.setObjectName("details")
        bookisAvailable = QLabel()
        bookisAvailable.setText("Availability: Available")
        bookisAvailable.setObjectName("details")

        bookBorrowedDate = QLabel()
        bookBorrowedDate.setText(book.borrowedDate)
        bookBorrowedDate.setObjectName("details")

        bookYear = QLabel()
        bookYear.setText(book.publishingYear)
        bookYear.setObjectName("details")

        bookPublisher = QLabel()
        bookPublisher.setText(book.publisher)
        bookPublisher.setObjectName("details")

        testLabelDesc = QLabel()
        testLabelDesc.setObjectName("details")
        testLabelDesc.setText(
            "DescDescDescDescDescDesc\nDescDescDescDescDesc\nDescDescDescDescDescDesc\nDescDescDescDescDesc\nDescDescDesc")

        self.textContainerVertLayout = QVBoxLayout()
        self.textContainerVertLayout.addWidget(bookAuthor)
        self.textContainerVertLayout.addWidget(bookGenre)
        self.textContainerVertLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.textContainerVertLayout.addWidget(bookRating)
        self.textContainerVertLayout.addWidget(bookisBorrowed)
        self.textContainerVertLayout.addWidget(testLabelDesc)
        # self.textContainerVertLayout2.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.textContainerHoriLayout.addLayout(self.textContainerVertLayout)
        # self.textContainerHoriLayout.addLayout(self.textContainerVertLayout2)
        self.textContainerHoriLayout.addStretch
        self.textContainer.setLayout(self.textContainerHoriLayout)
        
        self.containerVertLayout = QVBoxLayout()
        self.containerHoriLayout.addWidget(imageLabel)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)

        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        horilayout.addWidget(self.textContainer)
        
        
        if self.currentUser.userid == self.borrowedUserId:
            self.isBorrowedBtn = IsBorrowedBtn(BtnStatus.RETURN)
        elif self.borrowedUserId == 0:
            self.isBorrowedBtn = IsBorrowedBtn(BtnStatus.AVALABLE)
        else:
            self.isBorrowedBtn = IsBorrowedBtn(BtnStatus.UNAVALABLE)
        
        self.isBorrowedBtn.clicked.connect(self.borrowedBtnPressed)
        vertlayout = QVBoxLayout()
        vertlayout.addLayout(horilayout)
        vertlayout.addWidget(self.isBorrowedBtn)
        self.setLayout(vertlayout)
    
    def borrowedBtnPressed(self):
        currentStatues = self.isBorrowedBtn.getStatus()
        if currentStatues ==  BtnStatus.AVALABLE:
            print(self.currentUser.userid)
            insertBorrowedTable(self.currentUser, self.book)
            self.isBorrowedBtn.setStatus(BtnStatus.RETURN)
        elif currentStatues == BtnStatus.RETURN:
            removeBorrowedTable(self.book)
            self.isBorrowedBtn.setStatus(BtnStatus.AVALABLE)
        #self.borrowedBtnClicked.emit(self.isBorrowedBtn.getStatus())
        

        
        
        

class IsBorrowedBtn(QPushButton):
    def __init__(self, status: BtnStatus):
        super(QPushButton, self).__init__() 
        self.btnStatus = status
        self.setMaximumWidth(150)
        self.setMinimumHeight(40)
        self.setObjectName('isBorrowBtn')
        self.changeStatus()
        
    def setAvalible(self):
        self.setText('Borrow')
        self.setStyleSheet('background: green')
    
    def setUnavalible(self):
        self.setText('Unavalible')
        self.setStyleSheet('background: red')
        self.setEnabled(False)
    
    def setReturn(self):
        self.setText('Return')
        self.setStyleSheet('background: yellow')
    
    def changeStatus(self):
        if self.btnStatus == BtnStatus.AVALABLE:
            self.setAvalible()
        elif self.btnStatus == BtnStatus.UNAVALABLE:
            self.setUnavalible()
        elif self.btnStatus == BtnStatus.RETURN:
            self.setReturn()
    
    def getStatus(self):
        return self.btnStatus
    
    def setStatus(self, newStatus = BtnStatus.RETURN):
        self.btnStatus = newStatus
        self.changeStatus()