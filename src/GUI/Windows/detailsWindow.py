from GUI.elements.detailsView import DetailsView
from GUI.elements.header import CustHeader
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize


class DetailWindow(QFrame):
    def __init__(self, img, title, parent=None):
        super(QFrame, self).__init__()
        self.setWindowTitle("Details")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("detailsWindow")
        # self.setFrameShape(QFrame.Shape.NoFrame)
        # self.setLineWidth(0)

        self.header = CustHeader()
        self.details = DetailsView(img, title)
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.details)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)
