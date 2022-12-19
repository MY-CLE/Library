import sys
sys.path.insert(0, "src//")
import database.dbconnect as db
from functional.book import Book

class fetchBooks(object):

    def fetchAllBooks() -> list:
        bookArray = []
        data = db.DatabaseHandler()
        query = f"SELECT bookid FROM books;"
        array = data.parser(query)
        for i in array:
            x= int(i[0])
            bookArray.append(x)
            
        return bookArray    
           
    
    
def main():
    a = fetchBooks()
    for id in a.fetchAllBooks():
        print(id)
    
    
        
if __name__ == '__main__':
    main()