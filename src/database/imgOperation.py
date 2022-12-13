import io
import os
import sys

import psycopg2
from psycopg2 import BINARY, Binary
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from PIL import Image

class ImgOperation():
    db = DatabaseHandler()
    def insert(self,bookId,imgpath):
        
        with open(imgpath, "rb") as f:
            img_data = f.read()
        
       # print(len(str(img_binary)))
        
        query = f"UPDATE public.books SET picture = {bytes(img_data)} WHERE books.bookid = {bookId}"
        self.db.insert(query)

    def select(self,bookId):
        query = f"SELECT * FROM books WHERE books.bookid = {bookId}"
        img_data = self.db.parser(query)[0][9]
        print(len(img_data))
        path = os.path.join(os.path.abspath('src/assets/covers/'), f"cover_{bookId}_.jpg")
        
        img = Image.frombytes("RGB", (350, 523), bytes(img_data))
        img.save(path)
        """ if(img_data):
            with open(path, 'wb')as img:
                img.write(img_data)
                img.close()
         """
    
#if __name__ == "__main__:":
ip = ImgOperation()
path = os.path.join(os.path.abspath('src/assets/books/'), "50_shades_of_grey.jpg")
print(path)
ip.insert(1 , path),
ip.select(1)