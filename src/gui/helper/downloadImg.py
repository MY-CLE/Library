import os
import requests
from PyQt6.QtCore import pyqtSignal, pyqtSlot, QRunnable, QObject, QThreadPool
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QMainWindow, QLabel)
from PyQt6.QtGui import QPixmap, QImage
from GUI.Windows.detailsWindow import DetailWindow
from GUI.elements.detailsView import BookView


class DownloadImg(QRunnable):
    def __init__(self, dic):
        super().__init__()
        self.dic = dic
        self.signals = DownloadImgSignals()

    def run(self):
        self.dic['localpath'] = os.path.join(os.path.abspath(
            'src/assets/books/'), f"Image_{str(self.dic['id'])}.jpg")
        if not os.path.exists(self.dic['localpath']):
            img_data = requests.get(self.dic['img-src']).content
            with open(self.dic['localpath'], 'wb') as handler:
                handler.write(img_data)
        self.signals.returnBook.emit(self.dic)
        self.signals.finished.emit()


class DownloadImgSignals(QObject):
    returnBook = pyqtSignal(dict)
    finished = pyqtSignal()


class BookViewFunktions():

    def loadBooks(self, data):
        self.threadpool = QThreadPool().globalInstance()
        for count, book in enumerate(data):
            book['id'] = count
            worker = DownloadImg(book)
            worker.signals.returnBook.connect(self.bookRecived)
            worker.signals.finished.connect(
                lambda: self.workerfinished(len(data)))
            self.threadpool.tryStart(worker)

    def bookRecived(self, book):
        self.addBook(book)

    def workerfinished(self, len):
        if self.containerHoriLayout.count() >= len:
            self.containerHoriLayout.addStretch()

    def addBook(self, bookDic):

        self.book = QWidget()
        self.title = QLabel()
        self.title.setObjectName('bookTitleLable')

        if len(bookDic['title']) <= 20:
            self.title.setText(bookDic['title'])
        else:
            self.title.setText(bookDic['title'][:18] + '...')

        image = QImage(bookDic['localpath'])
        self.lable = PictureLabel(image)
        self.lable.setObjectName('bookCoveLable')

        bookLayout = QVBoxLayout()
        bookLayout.addStretch()
        bookLayout.addWidget(self.lable)
        bookLayout.addWidget(self.title)
        bookLayout.addStretch()
        self.book.setLayout(bookLayout)

        self.containerHoriLayout.addWidget(self.book)


class PictureLabel(QLabel):

    def __init__(self, image, parent=None):
        super(PictureLabel, self).__init__(parent)
        cover = QPixmap(image)
        cover = cover.scaledToHeight(200)
        self.setPixmap(cover)

    def mousePressEvent(self, event):
        #self.window = QMainWindow()
        self.stats = DetailWindow()
        self.stats.__init__()
        self.stats.show()
        # self.window.hide()
