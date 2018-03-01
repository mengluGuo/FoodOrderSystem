import sys
from PyQt5.QtWidgets import *
from Model.Model import Model
from Interfaces.Observer import Observer


class TablesLayout(Observer, QWidget):
    def __init__(self, model=Model()):
        super().__init__()
        self.__model = model
        self.__showTable1Area = QTextEdit()
        self.__showTable2Area = QTextEdit()
        self.__showTable3Area = QTextEdit()
        self.__showTable4Area = QTextEdit()
        self.__showTable5Area = QTextEdit()
        grid = QGridLayout()
        grid.addItem(self.setupTable1Layout(), 1, 0)
        grid.addItem(self.setupTable2Layout(), 1, 1)
        grid.addItem(self.setupTable3Layout(), 1, 2)
        grid.addItem(self.setupTable4Layout(), 1, 3)
        grid.addItem(self.setupTable5Layout(), 1, 4)
        self.setLayout(grid)
        # self.update()


    # method to setup the table1 layout
	# include a display list text area
	# @return a QHBoxLayout
    def setupTable1Layout(self):
        self.__showTable1Area.setDisabled(True)
        inner_layout_showTable1Area = QGridLayout()
        inner_layout_showTable1Area.addWidget(self.__showTable1Area)
        table1_groupbox = QGroupBox('Table 1')
        table1_groupbox.setLayout(inner_layout_showTable1Area)
        table1_layout = QHBoxLayout()
        table1_layout.addWidget(table1_groupbox)
        return table1_layout

    # method to setup the table2 layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupTable2Layout(self):
        self.__showTable2Area.setDisabled(True)
        inner_layout_showTable2Area = QGridLayout()
        inner_layout_showTable2Area.addWidget(self.__showTable2Area)
        table2_groupbox = QGroupBox('Table 2')
        table2_groupbox.setLayout(inner_layout_showTable2Area)
        table2_layout = QHBoxLayout()
        table2_layout.addWidget(table2_groupbox)
        return table2_layout

    # method to setup the table3 layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupTable3Layout(self):
        self.__showTable3Area.setDisabled(True)
        inner_layout_showTable3Area = QGridLayout()
        inner_layout_showTable3Area.addWidget(self.__showTable3Area)
        table3_groupbox = QGroupBox('Table 3')
        table3_groupbox.setLayout(inner_layout_showTable3Area)
        table3_layout = QHBoxLayout()
        table3_layout.addWidget(table3_groupbox)
        return table3_layout

    # method to setup the table4 layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupTable4Layout(self):
        self.__showTable4Area.setDisabled(True)
        inner_layout_showTable4Area = QGridLayout()
        inner_layout_showTable4Area.addWidget(self.__showTable4Area)
        table4_groupbox = QGroupBox('Table 4')
        table4_groupbox.setLayout(inner_layout_showTable4Area)
        table4_layout = QHBoxLayout()
        table4_layout.addWidget(table4_groupbox)
        return table4_layout

    # method to setup the table5 layout
    # include a display list text area
    # @return a QHBoxLayout
    def setupTable5Layout(self):
        self.__showTable5Area.setDisabled(True)
        inner_layout_showTable5Area = QGridLayout()
        inner_layout_showTable5Area.addWidget(self.__showTable5Area)
        table5_groupbox = QGroupBox('Table 5')
        table5_groupbox.setLayout(inner_layout_showTable5Area)
        table5_layout = QHBoxLayout()
        table5_layout.addWidget(table5_groupbox)
        return table5_layout

    def update(self):
        table1_list = self.__model.tableOneList
        table1_output = 'Ordered for Table One: \n%5s %9s %10s %5s\n' % ('ID', 'Dish', 'Quantity', 'Table')
        for order in table1_list:
            table1_output += '%5s %1s %10s %5s\n' % (order.sequenceID, order.dishName, order.quantity, order.tableID)
        self.__showTable1Area.setText(table1_output)

        table2_list = self.__model.tableTwoList
        table2_output = 'Ordered for Table Two: \n%5s %9s %10s %5s\n' % ('ID', 'Dish', 'Quantity', 'Table')
        for order in table2_list:
            table2_output += '%5s %1s %10s %5s\n' % (order.sequenceID, order.dishName, order.quantity, order.tableID)
        self.__showTable2Area.setText(table2_output)

        table3_list = self.__model.tableThreeList
        table3_output = 'Ordered for Table Three: \n%5s %9s %10s %5s\n' % ('ID', 'Dish', 'Quantity', 'Table')
        for order in table3_list:
            table3_output += '%5s %1s %10s %5s\n' % (order.sequenceID, order.dishName, order.quantity, order.tableID)
        self.__showTable3Area.setText(table3_output)

        table4_list = self.__model.tableFourList
        table4_output = 'Ordered for Table Fout: \n%5s %9s %10s %5s\n' % ('ID', 'Dish', 'Quantity', 'Table')
        for order in table4_list:
            table4_output += '%5s %1s %10s %5s\n' % (order.sequenceID, order.dishName, order.quantity, order.tableID)
        self.__showTable4Area.setText(table4_output)

        table5_list = self.__model.tableFiveList
        table5_output = 'Ordered for Table Five: \n%5s %9s %10s %5s\n' % ('ID', 'Dish', 'Quantity', 'Table')
        for order in table5_list:
            table5_output += '%5s %1s %10s %5s\n' % (order.sequenceID, order.dishName, order.quantity, order.tableID)
        self.__showTable5Area.setText(table5_output)
