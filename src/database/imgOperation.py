import io
import os
import sys
from psycopg2 import BINARY, Binary
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler

class ImgOperation():
    db = DatabaseHandler()
    def insert(self,bookId,imgpath):
        
        img_data = open(imgpath, "rb").read()        
        query = f"UPDATE public.books SET picture = {Binary(img_data)} WHERE books.bookid = {bookId}"
        self.db.insert(query)

    def select(self,bookId):
        path = os.path.join(os.path.abspath('src/assets/covers/'), f"cover_{bookId}_.jpg")
        query = f"SELECT * FROM books WHERE books.bookid = {bookId}"
        img_data = self.db.parser(query)[0][9]
        if(img_data):
            with open(path, 'wb')as img:
                img.write(io.BytesIO(img_data))
                img.close()
    
#if __name__ == "__main__:":
ip = ImgOperation()
path = os.path.join(os.path.abspath('src/assets/books/'), "50_shades_of_grey.jpg")
print(path)
ip.insert(1 , path),
ip.select(1)