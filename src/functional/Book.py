
class Book(object):

    def __init__(self, title: str, author: str, publishingYear: int, edition: str, publisher: str) -> None:
        self.__title = title
        self.__author = author
        self.__publishingYear = publishingYear
        self.__edition = edition
        self.__publisher = publisher
        self.__ratings: rating = []
        self.__isBorrowed: bool = False
