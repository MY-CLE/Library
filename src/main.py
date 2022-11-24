import sys
sys.path.insert(0,'src//')
from GUI.pageselect import PageSelect
import os
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    
    root = os.getcwd()
    stylesheet = os.path.join(root, os.path.abspath("src/GUI/styles.qss"))
    
    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())
        
    application = PageSelect()
    app.exec()
        
if __name__ == "__main__":
    main()