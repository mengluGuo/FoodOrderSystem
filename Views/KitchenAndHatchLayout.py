import sys
from PyQt5.QtWidgets import *


class KitchenAndHatchLayout(QWidget):
    def __init__(self, model, width, height):
        super().__init__()
        grid = QGridLayout()
        grid.addItem(self.setupKitchenLayout(), 1, 0)
        grid.addItem(self.setupHatchLayout(), 1, 1)
        self.setLayout(grid)

    # method to setup the kitchen layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupKitchenLayout(self):
        self.__showKitchenArea = QTextEdit()
        self.__showKitchenArea.setDisabled(True)
        inner_layout__showKitchenArea = QGridLayout()
        inner_layout__showKitchenArea.addWidget(self.__showKitchenArea)
        kitchen_groupbox = QGroupBox('Kitchen Order List')
        kitchen_groupbox.setLayout(inner_layout__showKitchenArea)
        kitchen_layout = QHBoxLayout()
        kitchen_layout.addWidget(kitchen_groupbox)
        return kitchen_layout

    # method to setup the hatch layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupHatchLayout(self):
        self.__showHatchArea = QTextEdit()
        self.__showHatchArea.setDisabled(True)
        inner_layout__showHatchArea = QGridLayout()
        inner_layout__showHatchArea.addWidget(self.__showHatchArea)
        hatch_groupbox = QGroupBox('Hatch Order List')
        hatch_groupbox.setLayout(inner_layout__showHatchArea)
        hatch_layout = QHBoxLayout()
        hatch_layout.addWidget(hatch_groupbox)
        return hatch_layout