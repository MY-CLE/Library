import sys
sys.path.insert(0, "src//")
import database.dbconnect as db
import functional.Book as book

class fetchBooks(object):

    def fetchAllBooks(self) -> list:
        bookArray = []
        temp1:str
        temp2:bytes
        data = db.DatabaseHandler()
        self.query = f"SELECT book_name, book_picture FROM books;"
        array = data.parser(self.query)
        for i in range(len(array)):
            for j in range(len(array[i])):
                if (j == 0):
                    temp1 = array[i][j]
                else:
                    temp2 = array[i][j]
                    
            bookArray.append(book.Book(temp1,temp2))
        return bookArray
    
    
def main():
    a = fetchBooks()
    #for book in a.fetchAllBooks():
        #print(book.getBookName())
        #print(book.getBookPicture())
    
    
        
if __name__ == '__main__':
    main()