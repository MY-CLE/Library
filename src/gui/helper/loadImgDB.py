
import sys
from time import sleep
sys.path.insert(0, "src//")
from database.fetchCertainBook import fetchCertainBook
from PyQt6.QtCore import pyqtSignal, QRunnable, QObject, QThreadPool
from functional.book import Book

class LoadBook(QRunnable):
    def __init__(self, bookNo):
        super().__init__()
        self.bookNo = bookNo
        self.signals = LoadBookSignals()

    def run(self):
        #print(f'in Load book {self.bookNo}')
        bookfetcher = fetchCertainBook()
        book = bookfetcher.fetchCertainBook(self.bookNo)
        self.signals.returnBook.emit(book)
        
class  LoadBookSignals(QObject):
    returnBook = pyqtSignal(Book)
    
    
class Bookloader(QObject):
    threadpool = QThreadPool().globalInstance()
    bookloaded = pyqtSignal(Book) 
    
    def loadBook(self, bookNo):
        #print('loadBook started in book loader')
        worker = LoadBook(bookNo)
        worker.signals.returnBook.connect(self.bookRecived)
        savety = 50
        while not self.threadpool.tryStart(worker) and savety :
            sleep(0.5)
            savety -=1
    
    def bookRecived(self, book):
        print(book)
        self.bookloaded.emit(book)
                
        
        
        
    