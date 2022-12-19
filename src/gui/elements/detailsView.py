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
        self.textContainer.setMinimumWidth(300)
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
        bookAuthor.setText("Author: "+book.getAuthor())
        bookAuthor.setObjectName("details")

        imgpath = os.path.join(os.path.abspath(
            'src/assets/books/'), book.getPicture())
        image = QImage(imgpath)
        bookCover = QPixmap(image)
        bookCover = bookCover.scaledToHeight(200)
        bookCover = bookCover.scaledToWidth(200)
        imageLabel = QLabel()
        imageLabel.setPixmap(bookCover)

        bookGenre = QLabel()
        bookGenre.setText("Genre: "+book.getGenre())
        bookGenre.setObjectName("details")

        bookRating = QLabel()
        bookRating.setText(f"Rating: {book.getAverageRating()}")
        bookRating.setObjectName("details")

        bookisBorrowed = QLabel()
        bookisBorrowed.setText("Availability: Unavailable")
        bookisBorrowed.setObjectName("details")
        bookisAvailable = QLabel()
        bookisAvailable.setText("Availability: Available")
        bookisAvailable.setObjectName("details")

        bookBorrowedDate = QLabel()
        bookBorrowedDate.setText(book.getBorrowedDate())
        bookBorrowedDate.setObjectName("details")

        bookYear = QLabel()
        bookYear.setText(book.getPublishingYear())
        bookYear.setObjectName("details")

        bookPublisher = QLabel()
        bookPublisher.setText(book.getPublisher())
        bookPublisher.setObjectName("details")

        testLabelDesc = QLabel()
        testLabelDesc.setObjectName("details")
        testLabelDesc.setText(
            "DescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDesc")

        self.textContainerVertLayout = QVBoxLayout()
        self.textContainerVertLayout.addWidget(bookAuthor)
        self.textContainerVertLayout.addWidget(bookGenre)
        self.textContainerVertLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #self.textContainerVertLayout2 = QVBoxLayout()
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
        self.setLayout(horilayout)
