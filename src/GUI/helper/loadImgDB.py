
import sys
sys.path.insert(0, "src//")
from database.fetchCertainBook import fetchCertainBook
import os
from PyQt6.QtCore import pyqtSignal, pyqtSlot, QRunnable, QObject, QThreadPool

class LoadBook(QRunnable):
    def __init__(self, bookNo):
        super().__init__()
        self.bookNo = bookNo
        self.signals = LoadBookSignals()

    def run(self):
        print(f'in Load book {self.bookNo}')
        bookfetcher = fetchCertainBook()
        bookinfo = bookfetcher.fetchCertainBook(self.bookNo)
        self.signals.returnBook.emit(bookinfo)
        self.signals.finished.emit()
        
class LoadBookSignals(QObject):
    returnBook = pyqtSignal(dict)
    finished = pyqtSignal()
    
    
class Bookloader(QObject):
    threadpool = QThreadPool().globalInstance()
    bookloaded = pyqtSignal(dict) 
    
    def loadBook(self, bookNo):
        print('loadBook started in book loader')
        worker = LoadBook(bookNo)
        worker.signals.returnBook.connect(self.bookRecived)
        self.threadpool.tryStart(worker)
    
    def bookRecived(self, dic):
        print(dic)
        self.bookloaded.emit(dic)
                
        
        
        
    