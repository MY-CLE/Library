import sys
sys.path.insert(0, "src//")
import database.dbconnect as db
import functional.Book as book

class fetchBooks(object):

    def fetchAllBooks(self) -> list:
        bookArray = []
        bookDict:dict
        title:str
        author:str
        picture:bytes
        data = db.DatabaseHandler()
        self.query = f"SELECT title,author,picture FROM books;"
        array = data.parser(self.query)
        for i in range(len(array)):
            for j in range(len(array[i])):
                if (j == 0):
                    title = array[i][j]
                elif (j==1):
                    author = array[i][j]
                else:
                    picture = array[i][j]
            bookDict = {"title":title,"author":author,"picture":picture}    
            bookArray.append(bookDict)
        return bookArray
    
    
def main():
    a = fetchBooks()
    
    for book in a.fetchAllBooks():
        print(book)
    
    
        
if __name__ == '__main__':
    main()