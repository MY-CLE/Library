import json
import os
from PyQt6.QtWidgets import (
    QHBoxLayout, QLayout, QVBoxLayout, QFrame, QWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage

from database.dbfunctions import fetchBook


class DetailsView(QFrame):
    def __init__(self, bookId):
        super(QFrame, self).__init__()
        self.setObjectName('libraryView')
        self.bookView = BookView(bookId)
        self.titleView = TitleView(bookId)
        mainVertLayout = QVBoxLayout()
        HoriLayout = QHBoxLayout()
        HoriLayout.addWidget(self.bookView)
        mainVertLayout.addWidget(self.titleView)
        mainVertLayout.addWidget(self.bookView)
        self.setLayout(mainVertLayout)


class TitleView(QFrame):
    def __init__(self, bookId):
        super(QFrame, self).__init__()

        book = fetchBook(bookId)
        title = QLabel()
        title.setText(book.getTitle())
        title.setObjectName('titleView')

        HoriLayout = QHBoxLayout()
        HoriLayout.addWidget(title)
        self.setLayout(HoriLayout)


class BookView(QFrame):
    def __init__(self, bookId):
        super(QFrame, self).__init__()
        self.setObjectName('bookView')
        self.container = QWidget()
        self.container.setObjectName("bookViewContainer")
        self.container.setMaximumWidth(300)
        self.container.setMaximumHeight(300)

        self.textContainer = QWidget()
        self.textContainer.setObjectName("bookViewContainer")
        self.textContainer.setMinimumWidth(200)
        self.textContainer.setMaximumHeight(300)

        self.containerHoriLayout = QHBoxLayout()
        self.containerHoriLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.textContainerHoriLayout = QHBoxLayout()
        # self.textContainerHoriLayout.setAlignment(
        # Qt.AlignmentFlag.AlignHCenter)

        book = fetchBook(bookId)

        bookTitle = QLabel()
        bookTitle.setText(book.getTitle())

        bookAuthor = QLabel()
        authorContainer = QWidget()
        authorContainer.setObjectName("details")
        authorContainer.setMinimumWidth(30)
        authorContainer.setMaximumHeight(20)
        authorContainerHoriLayout = QHBoxLayout()
        bookAuthor.setText(book.getAuthor())

        imgpath = os.path.join(os.path.abspath(
            'src/assets/books/'), book.getPicture())
        image = QImage(imgpath)
        bookCover = QPixmap(image)
        bookCover = bookCover.scaledToHeight(200)
        bookCover = bookCover.scaledToWidth(200)
        imageLabel = QLabel()
        imageLabel.setPixmap(bookCover)

        bookGenre = QLabel()
        bookGenre.setText(book.getGenre())
        bookGenre.setObjectName("details")

        bookRating = QLabel()
        bookRating.setNum(book.getAverageRating())

        bookisBorrowed = QLabel()
        bookisBorrowed.setText("Unavailable")
        bookisAvailable = QLabel()
        bookisAvailable.setText("Available")

        bookBorrowedDate = QLabel()
        bookBorrowedDate.setText(book.getBorrowedDate())

        bookYear = QLabel()
        bookYear.setText(book.getPublishingYear())

        bookPublisher = QLabel()
        bookPublisher.setText(book.getPublisher())

        book.printEverything()

        self.textContainerVertLayout = QVBoxLayout()
        authorContainerHoriLayout.addWidget(bookAuthor)
        authorContainer.setLayout(self.textContainerHoriLayout)
        self.textContainerVertLayout.addWidget(authorContainer)
        self.textContainer.setLayout(self.textContainerVertLayout)

        self.containerVertLayout = QVBoxLayout()
        self.containerHoriLayout.addWidget(imageLabel)
        self.containerVertLayout.addLayout(self.containerHoriLayout)
        self.container.setLayout(self.containerVertLayout)

        horilayout = QHBoxLayout()
        horilayout.addWidget(self.container)
        horilayout.addWidget(self.textContainer)
        self.setLayout(horilayout)
