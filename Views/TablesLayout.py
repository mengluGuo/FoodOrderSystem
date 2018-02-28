import sys
from PyQt5.QtWidgets import *


class TablesLayout(QWidget):
    def __init__(self, model):
        super().__init__()
        grid = QGridLayout()
        grid.addItem(self.setupTable1Layout(), 1, 0)
        grid.addItem(self.setupTable2Layout(), 1, 1)
        grid.addItem(self.setupTable3Layout(), 1, 2)
        grid.addItem(self.setupTable4Layout(), 1, 3)
        grid.addItem(self.setupTable5Layout(), 1, 4)
        self.setLayout(grid)

    def setupTable1Layout(self):
        ...

    def setupTable2Layout(self):
        ...

    def setupTable3Layout(self):
        ...

    def setupTable4Layout(self):
        ...

    def setupTable5Layout(self):
        ...