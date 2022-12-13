import sys
sys.path.insert(0, "src//")
import database.dbconnect as db
import functional.book as Book

class fetchCertainBook(object):

    def fetchCertainBook(self, signal) -> dict:
        bookDict:dict
        title:str
        author:str
        picture:bytes
        data = db.DatabaseHandler()
        self.query = f"SELECT bookid,title,author,genre,publishingyear,borroweddate,publisher,rating,isborrowed,picture FROM books WHERE bookid={signal};"
        array = data.parser(self.query)
        bookDict = {"bookid":self.fetchId(array),"title":self.fetchTitle(array),"author":self.fetchAuthor(array),"genre":self.fetchGenre(array),
                    "publishingyear":self.fetchPublishingYear(array), "borroweddate":self.fetchBorrowedDate(array),"publisher":self.fetchPublisher(array),
                    "rating":self.fetchRating(array),"isborrowed":self.fetchIsBorrowed(array),"picture":self.fetchPicture(array)}
        return bookDict
    
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
    
    def fetchBorrowedDate(self, bookArr):
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
    print(a.fetchCertainBook(1))
    
        
if __name__ == '__main__':
    main()