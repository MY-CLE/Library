import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book
from datetime import date

class fetchCertainBook(object):

    def fetchCertainBook(self, signal) -> Book:
        title:str
        author:str
        picture:bytes
        data = DatabaseHandler()
        self.query = f"SELECT bookid, title, author, genre, publishingyear, borrowedDate, publisher, rating, isBorrowed, picturepath FROM books WHERE bookid={signal};"
        array = data.parser(self.query)
        certainBook = Book(self.fetchId(array),self.fetchTitle(array),self.fetchAuthor(array),self.fetchGenre(array),
                    self.fetchPublishingYear(array),self.fetchBorrowedDate(array),self.fetchPublisher(array),
                    self.fetchRating(array),self.fetchIsBorrowed(array),self.fetchPicture(array))
        return certainBook

    def fetchId(self, bookArr) -> int:
        return bookArr[0][0]
    
    def fetchTitle(self, bookArr) -> str:
        return bookArr[0][1]
    
    def fetchAuthor(self, bookArr) -> str:
        return bookArr[0][2]
    
    def fetchGenre(self, bookArr) -> str:
        return bookArr[0][3]
    
    def fetchPublishingYear(self, bookArr) -> int:
        return bookArr[0][4]
    
    def fetchBorrowedDate(self, bookArr)-> date:
        return bookArr[0][5]
    
    def fetchPublisher(self, bookArr) -> str:
        return bookArr[0][6]
    
    def fetchRating(self, bookArr) -> float:
        return bookArr[0][7]
    
    def fetchIsBorrowed(self, bookArr) -> bool:
        return bookArr[0][8]
    
    def fetchPicture(self, bookArr) -> str:
        return bookArr[0][9]
    
    
    
def main():
    a = fetchCertainBook()
    a.fetchCertainBook(1).printEverything()
    
        
if __name__ == '__main__':
    main()