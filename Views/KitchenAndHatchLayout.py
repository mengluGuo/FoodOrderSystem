import sys
from PyQt5.QtWidgets import *
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
        kitchen_output = 'Waiting for cooking\n%-20s %-11s %-13s %-7s\n' % ('ID', 'DishName', 'Quantity', 'Table')
        if kitchen_list is not None and len(kitchen_list)>0:
            for uncooked_order in kitchen_list:
                kitchen_output += '%-10s %-10s %-15s %-7s\n' % (uncooked_order.sequenceID,
                                                            uncooked_order.dishName,
                                                            uncooked_order.quantity,
                                                            uncooked_order.tableID)
        # self.__showKitchenArea.setText(kitchen_output)


        hatch_list = self.__model.hatchList
        hatch_output = 'Waiting for delivery\n %-20s %-11s %-13s %-7s\n' % ('ID', 'DishName', 'Quantity', 'Table')
        for cooked_order in hatch_list:
            hatch_output += '%-10s %-10s %-15s %-7s\n' % (cooked_order.sequenceID,
                                                      cooked_order.dishName,
                                                      cooked_order.quantity,
                                                      cooked_order.tableID)
        # self.__showHatchArea.setText(hatch_output)
