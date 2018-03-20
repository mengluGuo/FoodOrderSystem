import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
from Model.Model import Model
from Interfaces.Observer import Observer


class KitchenAndHatchLayout(Observer, QWidget):
    def __init__(self, model=Model()):
        super().__init__()
        self.__model = model
        self.__model.registerObserver(self)
        self.__showKitchenArea = QTextEdit()
        self.__showHatchArea = QTextEdit()
        grid = QGridLayout()
        grid.addItem(self.setupKitchenLayout(), 1, 0)
        grid.addItem(self.setupHatchLayout(), 1, 1)
        self.setLayout(grid)

        self.__kitchenarea_text = ''
        self.__hatch_output = ''

        self.__monitor = Monitor()
        self.__monitor.updateText.connect(self.setText)

        self.update()

    # method to setup the kitchen layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupKitchenLayout(self):
        self.__showKitchenArea.setDisabled(True)
        inner_layout_showKitchenArea = QGridLayout()
        inner_layout_showKitchenArea.addWidget(self.__showKitchenArea)
        kitchen_groupbox = QGroupBox('Kitchen Order List')
        kitchen_groupbox.setLayout(inner_layout_showKitchenArea)
        kitchen_layout = QHBoxLayout()
        kitchen_layout.addWidget(kitchen_groupbox)
        return kitchen_layout

    # method to setup the hatch layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupHatchLayout(self):
        self.__showHatchArea.setDisabled(True)
        inner_layout__showHatchArea = QGridLayout()
        inner_layout__showHatchArea.addWidget(self.__showHatchArea)
        hatch_groupbox = QGroupBox('Hatch Order List')
        hatch_groupbox.setLayout(inner_layout__showHatchArea)
        hatch_layout = QHBoxLayout()
        hatch_layout.addWidget(hatch_groupbox)
        return hatch_layout

    def update(self):
        kitchen_list = self.__model.getKitchenList()
        kitchen_output = 'Waiting for cooking\n%-5s %-11s %-13s %-7s\n' % ('ID', 'DishName', 'Quantity', 'Table')
        if kitchen_list is not None and len(kitchen_list)>0:
            for uncooked_order in kitchen_list:
                kitchen_output += '%-5s %-15s %-10s %-7s\n' % (uncooked_order.sequenceID,
                                                            uncooked_order.dishName,
                                                            uncooked_order.quantity,
                                                            uncooked_order.tableID)
                self.__kitchenarea_text = kitchen_output

        hatch_list = self.__model.hatchList
        hatch_output = 'Waiting for delivery\n %-5s %-11s %-13s %-7s\n' % ('ID', 'DishName', 'Quantity', 'Table')
        for cooked_order in hatch_list:
            hatch_output += '%-5s %-15s %-10s %-7s\n' % (cooked_order.sequenceID,
                                                      cooked_order.dishName,
                                                      cooked_order.quantity,
                                                      cooked_order.tableID)

            self.__hatch_output = hatch_output

        self.__monitor.update_list()

    def setText(self):
        self.__showKitchenArea.setText(self.__kitchenarea_text)
        self.__showHatchArea.setText(self.__hatch_output)


class Monitor(QtCore.QObject):

    updateText = QtCore.pyqtSignal(str)

    def update_list(self):
        self.updateText.emit('updated list')