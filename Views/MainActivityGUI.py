import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Model.Model import Model
from Interfaces.ThreadListener import ThreadListener
from Threads.DeliveryWaiterThread import DeliveryWaiterThread
from Threads.KitchenThread import KitchenThread
from Threads.OrderWaiterThread import OrderWaiterThread
from CustomExceptions.CustomExceptions import TableIDNotFoundException
from CustomExceptions.CustomExceptions import NegativeNumberException
from Views.KitchenAndHatchLayout import KitchenAndHatchLayout
from Views.TablesLayout import TablesLayout
from Views.WaitersLayout import WaitersLayout


class MainActivityGUI(ThreadListener, QWidget):
    def __init__(self, model=Model()):
        super().__init__()
        self.__model = model

        self.__kitchenHatchLayout = KitchenAndHatchLayout(self.__model)
        self.__tablesLayout = TablesLayout(self.__model)
        self.__waitersLayout = WaitersLayout(self.__model)

        self.__switchButton = None
        self.__getBillButton = None
        self.__getReportButton = None
        self.__speedControlSlider = None
        self.__showBillArea = None
        self.__showReportArea = None

        # self.__width = 1000
        # self.__height = 650

        self.__orderWaiterThread = None
        self.__kitchenThread = None
        self.__deliveryThread = None

        control_layout = self.setupControlLayout()
        display_layout = self.setupDisplayLayout()

        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addItem(control_layout)
        grid.addItem(display_layout)
        grid.addWidget(self.__tablesLayout)
        grid.addWidget(self.__waitersLayout)

        self.setLayout(grid)
        self.setWindowTitle('FoodOrderSystem')
        self.show()

    # method to setup the display panel
    # include the kitchen and hatch panel, the tables panel
	# the show table bill panel and show report panel
    def setupDisplayLayout(self):
        # setup bill display layout
        self.__showBillArea = QTextEdit()
        self.__showBillArea.setDisabled(True)
        inner_layout_showBillArea = QGridLayout()
        inner_layout_showBillArea.addWidget(self.__showBillArea)
        bill_groupbox = QGroupBox('Bill Of Single Table')
        bill_groupbox.setLayout(inner_layout_showBillArea)
        bill_layout = QHBoxLayout()
        bill_layout.addWidget(bill_groupbox)

        # setup report display layout
        self.__showReportArea = QTextEdit()
        self.__showReportArea.setDisabled(True)
        inner_layout__showReportArea = QGridLayout()
        inner_layout__showReportArea.addWidget(self.__showReportArea)
        report_groupbox = QGroupBox('Complete Report')
        report_groupbox.setLayout(inner_layout__showReportArea)
        report_layout = QHBoxLayout()
        report_layout.addWidget(report_groupbox)

        display_layout = QGridLayout()
        display_layout.addWidget(self.__kitchenHatchLayout, 1, 0)
        display_layout.addItem(bill_layout, 1, 1)
        display_layout.addItem(report_layout, 1, 2)
        return display_layout

    def setupControlLayout(self):
        control_layout = QGridLayout()
        control_layout.setSpacing(5)

        # setup switch button
        self.__switchButton = QPushButton('Start')
        self.__switchButton.clicked.connect(self.switchButtonAction)
        control_layout.addWidget(self.__switchButton, 1, 0)

        # setup get bill button
        self.__getBillButton = QPushButton('Get Bill')
        control_layout.addWidget(self.__getBillButton, 1, 1)

        # setup get report button
        self.__getReportButton = QPushButton('Get Report')
        control_layout.addWidget(self.__getReportButton, 1, 2)

        # setup speed control slider
        speed_lable = QLabel(' Speed Control: ')
        self.__speedControlSlider = QSlider(Qt.Horizontal)
        self.__speedControlSlider.setFocusPolicy(Qt.StrongFocus)
        self.__speedControlSlider.setTickPosition(QSlider.TicksBothSides)
        self.__speedControlSlider.setTickInterval(10)
        self.__speedControlSlider.setSingleStep(1)
        # self.__speedControlSlider.setMinimum(1)
        # self.__speedControlSlider.setMaximum(10)
        # self.__speedControlSlider.setValue(5)
        speed_layout = QGridLayout()
        speed_layout.addWidget(speed_lable, 1, 0)
        speed_layout.addWidget(self.__speedControlSlider, 1, 1)
        control_layout.addItem(speed_layout, 1, 3)
        return control_layout

    def switchButtonAction(self):
        print("Click Start")
        if self.__orderWaiterThread is None:
            self.__orderWaiterThread = OrderWaiterThread(self.__model)
        if self.__kitchenThread is None:
            self.__kitchenThread = KitchenThread(self.__model)
        if self.__deliveryThread is None:
            self.__deliveryThread = DeliveryWaiterThread(self.__model)
        if self.__switchButton.text() is 'Start':
            self.__orderWaiterThread.start()
            self.__orderWaiterThread.runnable = True
            self.__kitchenThread.start()
            self.__kitchenThread.runnable = True
            self.__deliveryThread.start()
            self.__deliveryThread.runnable = True
            self.__switchButton.setText('Stop')
        else:



model = Model
app = QApplication(sys.argv)
ex = MainActivityGUI(model)
sys.exit(app.exec_())
