from gui.elements.detailsView import DetailsView
from gui.elements.header import CustHeader
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize


class DetailWindow(QFrame):
    def __init__(self,bookNo, parent=None):
        super(QFrame, self).__init__()
        self.bookNo = bookNo
        self.setWindowTitle("Details")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("detailsWindow")
        # self.setFrameShape(QFrame.Shape.NoFrame)
        # self.setLineWidth(0)

        self.header = CustHeader()
        self.details = DetailsView(bookNo)
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.details)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)
