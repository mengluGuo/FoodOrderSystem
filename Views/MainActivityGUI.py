import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
import logging

class MainActivityGUI(ThreadListener, QWidget):
    def __init__(self, model, conroller):
        super().__init__()
        self.__model = model

        self.__conroller = conroller

        self.__kitchenHatchLayout = KitchenAndHatchLayout(self.__model)
        self.__tablesLayout = TablesLayout(self.__model)
        self.__waitersLayout = WaitersLayout(self.__model)

        self.__switchButton = QPushButton('Start')
        self.__getBillButton = QPushButton('Get Bill')
        self.__getReportButton = QPushButton('Get Report')
        self.__speedControlSlider = QSlider(Qt.Horizontal)
        self.__showBillArea = QTextEdit()
        self.__showReportArea = QTextEdit()

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
        self.__showBillArea.setDisabled(True)
        inner_layout_showBillArea = QGridLayout()
        inner_layout_showBillArea.addWidget(self.__showBillArea)
        bill_groupbox = QGroupBox('Bill Of Single Table')
        bill_groupbox.setLayout(inner_layout_showBillArea)
        bill_layout = QHBoxLayout()
        bill_layout.addWidget(bill_groupbox)

        # setup report display layout
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
        self.__switchButton.clicked.connect(self.switchButtonAction)
        control_layout.addWidget(self.__switchButton, 1, 0)

        # setup get bill button
        self.__getBillButton.setEnabled(False)
        self.__getReportButton.setEnabled(False)
        self.__getBillButton.clicked.connect(self.getBillButionAction)
        control_layout.addWidget(self.__getBillButton, 1, 1)

        # setup get report button
        self.__getReportButton.clicked.connect(self.getReportButtonAction)
        control_layout.addWidget(self.__getReportButton, 1, 2)

        # setup speed control slider
        speed_lable = QLabel(' Speed Control: ')
        self.__speedControlSlider.setFocusPolicy(Qt.StrongFocus)
        self.__speedControlSlider.setTickPosition(QSlider.TicksBothSides)
        self.__speedControlSlider.setTickInterval(10)
        self.__speedControlSlider.setSingleStep(1)
        self.__speedControlSlider.setValue(5)
        self.__speedControlSlider.valueChanged.connect(self.__conroller.valuechange)
        # self.__speedControlSlider.setMinimum(1)
        # self.__speedControlSlider.setMaximum(10)
        # self.__speedControlSlider.setValue(5)
        speed_layout = QGridLayout()
        speed_layout.addWidget(speed_lable, 1, 0)
        speed_layout.addWidget(self.__speedControlSlider, 1, 1)
        control_layout.addItem(speed_layout, 1, 3)
        return control_layout

    def switchButtonAction(self):
        if self.__orderWaiterThread is None:
            self.__orderWaiterThread = OrderWaiterThread(self.__model)

        if self.__kitchenThread is None:
            self.__kitchenThread = KitchenThread(self.__model)

        if self.__deliveryThread is None:
            self.__deliveryThread = DeliveryWaiterThread(self, self.__model)

        if self.__switchButton.text() == 'Start':
            self.__orderWaiterThread.runnable = True
            self.__orderWaiterThread.start()
            self.__kitchenThread.runnable = True
            self.__kitchenThread.start()
            self.__deliveryThread.runnable = True
            self.__deliveryThread.start()
            self.__switchButton.setText('Stop')
            self.__getBillButton.setEnabled(False)
            self.__getReportButton.setEnabled(False)
        else:
            self.__orderWaiterThread.runnable = False
            self.__kitchenThread.runnable = False
            self.__deliveryThread.runnable = False
            self.__switchButton.setText('Start')
            self.__getBillButton.setEnabled(True)
            self.__getReportButton.setEnabled(True)

    def getBillButionAction(self):
        table_id, ok = QInputDialog.getText(self, 'Table ID input Dialog', 'Please Enter Table ID: ')
        bill = ''
        if ok:
            try:
                bill = self.__model.reportGenerator.getBillByTableID(int(table_id))
                self.__showBillArea.setText(bill)
            except TableIDNotFoundException as e:
                logging.error(e.message)
            except NegativeNumberException as e:
                logging.error(e.message)
            self.__model.writeIntoFile('table_bill.txt', bill)
            QMessageBox.about(self, 'Print Bill', 'Table bill have been print into table_bill.tx')

    def getReportButtonAction(self):
        completeReport = ''
        try:
            completeReport += self.__model.reportGenerator.getFinalReport()
        except TableIDNotFoundException as e:
            logging.error(e.message)
        except NegativeNumberException as e:
            logging.error(e.message)
        self.__showReportArea.setText(completeReport)
        self.__model.writeIntoFile('table_Report.txt', completeReport)
        QMessageBox.about(self, 'Complete report have been print into table_report.txt')

    def changeButtonStatus(self, flag):
        self.__getBillButton.setDisabled(flag)
        self.__getReportButton.setDisabled(flag)

    def getselfSpeedControlSlider(self):
        return self.__speedControlSlider

# model = Model()
# app = QApplication(sys.argv)
# ex = MainActivityGUI(model)
# sys.exit(app.exec_())
