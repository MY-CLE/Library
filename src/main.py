import sys
import os
from gui.pageselect import PageSelect
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon


if __name__ == "__main__":

    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("src/assets/logo/hse-library-book-icon.jpg"))
    root = os.getcwd()
    stylesheet = os.path.join(root, os.path.abspath("src/gui/styles.qss"))

    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())

    application = PageSelect()
    application.show()
    app.exec()



