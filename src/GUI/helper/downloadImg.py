import os
import requests
from PyQt6.QtCore import pyqtSignal, QRunnable, QObject, QThreadPool
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QLineEdit, )
from PyQt6.QtGui import QPixmap, QImage
class DownloadImg(QRunnable):
    def __init__(self, dic) :
        super().__init__()
        self.dic = dic
        self.signals = DownloadImgSignals()
    
    def run(self):
        self.dic['localpath'] = os.path.abspath(os.path.join('src/assets/covers/', f"Image_{str(self.dic['id'])}.jpg"))
        print(os.path.exists(self.dic['localpath']))
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
            worker.signals.finished.connect(lambda: self.workerfinished(len(data)))
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
        self.lable = QLabel()
        self.lable.setObjectName('bookCoveLable')
        cover = QPixmap(bookDic['localpath'])
        cover = cover.scaledToHeight(200)
        self.lable.setPixmap(cover)
        
        bookLayout = QVBoxLayout()
        bookLayout.addStretch()
        bookLayout.addWidget(self.lable)
        bookLayout.addWidget(self.title)
        bookLayout.addStretch()
        self.book.setLayout(bookLayout)
        
        self.containerHoriLayout.addWidget(self.book)