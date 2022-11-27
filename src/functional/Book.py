class Book(object):

    def __init__(self, title: str, author: str, publishingYear: int, edition: str, publisher: str) -> None:
        self.__title = title
        self.__author = author
        self.__publishingYear = publishingYear
        self.__edition = edition
        self.__publisher = publisher
        self.__borrowed = False

    def getTitle(self) -> str:
        return self.__title

    def setTitle(self, title: str) -> None:
        self.__title = title

    def getAuthor(self) -> str:
        return self.__author

    def setAuthor(self, author: str) -> None:
        self.__author = author

    def getPublishingYear(self) -> int:
        return self.__publishingYear

    def setPublishingYear(self, publishingYear: int) -> None:
        self.__publishingYear = publishingYear

    def getEdition(self) -> str:
        return self.__edition

    def setEdition(self, edition: str) -> None:
        self.__edition = edition

    def getPublisher(self) -> str:
        return self.__publisher

    def setPublisher(self, publisher: str) -> None:
        self.__publisher = publisher
    


