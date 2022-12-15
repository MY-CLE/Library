import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book

class fetchCertainBook(object):

    def fetchCertainBook(self, signal) -> dict:
        bookDict:dict
        title:str
        author:str
        picture:bytes
        data = DatabaseHandler()
        self.query = f"SELECT bookid, title, author, genre, publishingyear, borrowedDate, publisher, rating, isBorrowed, picture FROM books WHERE bookid={signal};"
        array = data.parser(self.query)[0]
        bookDict = {"bookid":self.fetchId(array),"title":self.fetchTitle(array),"author":self.fetchAuthor(array),"genre":self.fetchGenre(array),
                    "publishingyear":self.fetchPublishingYear(array), "borroweddate":self.fetchBorrowedDate(array),"publisher":self.fetchPublisher(array),
                    "rating":self.fetchRating(array),"isborrowed":self.fetchIsBorrowed(array),"picture":self.fetchPicture(array)}
        asbook = Book(bookDict["bookid"], bookDict["title"], bookDict["author"],bookDict["publishingyear"],"1", bookDict["publisher"],bookDict["rating"], bookDict["isborrowed"], bookDict["genre"], bookDict["borroweddate"], bookDict["picture"])
        
        return asbook
    
    def fetchId(self, bookArr) -> int:
        return bookArr[0]
    
    def fetchTitle(self, bookArr) -> str:
        return bookArr[1]
    
    def fetchAuthor(self, bookArr) -> str:
        return bookArr[2]
    
    def fetchGenre(self, bookArr) -> str:
        return bookArr[3]
    
    def fetchPublishingYear(self, bookArr) -> int:
        return bookArr[4]
    
    def fetchBorrowedDate(self, bookArr):
        return bookArr[5]
    
    def fetchPublisher(self, bookArr) -> str:
        return bookArr[6]
    
    def fetchRating(self, bookArr) -> float:
        return bookArr[7]
    
    def fetchIsBorrowed(self, bookArr) -> bool:
        return bookArr[8]
    
    def fetchPicture(self, bookArr) -> str:
        return bookArr[9]
    
    
    
def main():
    a = fetchCertainBook()
    print(a.fetchCertainBook(1))
    
        
if __name__ == '__main__':
    main()