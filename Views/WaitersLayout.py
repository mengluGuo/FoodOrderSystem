import sys
from PyQt5.QtWidgets import *
from Interfaces.Observer import Observer
from Model.Model import Model


class WaitersLayout(Observer, QWidget):
    def __init__(self, model=Model()):
        super().__init__()
        self.__model = model
        self.__model.registerObserver(self)
        self.__orderWaiterArea = QLineEdit()
        self.__deliveryWaiterArea = QLineEdit()
        grid = QGridLayout()
        grid.addItem(self.setupOrderWaiterLayout())
        grid.addItem(self.setupDeliveryWaiterLayout())
        self.setLayout(grid)
        self.update()

    # method to setup the order waiter layout
    # include a display list text area
    # @return a QGridLayout
    def setupOrderWaiterLayout(self):
        self.__orderWaiterArea.setDisabled(True)
        order_waiter_label = QLabel('Order Waiter:')
        order_waiter_grid = QGridLayout()
        order_waiter_grid.addWidget(order_waiter_label, 1, 0)
        order_waiter_grid.addWidget(self.__orderWaiterArea, 1, 1)
        return order_waiter_grid

    # method to setup the delivery waiter layout
    # include a display list text area
    # @return a QGridLayout
    def setupDeliveryWaiterLayout(self):
        self.__deliveryWaiterArea.setDisabled(True)
        delivery_waiter_label = QLabel('Delivery Waiter:')
        delivery_waiter_grid = QGridLayout()
        delivery_waiter_grid.addWidget(delivery_waiter_label, 1, 0)
        delivery_waiter_grid.addWidget(self.__deliveryWaiterArea, 1, 1)
        return delivery_waiter_grid

    def update(self):
        current_order = self.__model.order
        current_order_output = ''
        if current_order is not None:
            current_order_output = 'CURRENT ORDER: %-8s %-4s %-8s %-8s' % (current_order.sequenceID,
                                                                       current_order.dishName,
                                                                       current_order.quantity,
                                                                       current_order.tableID)
        self.__orderWaiterArea.setText(current_order_output)

        delivered_order = self.__model.deliveredOrder
        delivered_order_output = ''
        if delivered_order is not None:
            delivered_order_output = 'ORDER TO BE DELIVERED: %-8s %-4s %-8s %-8s' % (delivered_order.sequenceID,
                                                                                 delivered_order.dishName,
                                                                                 delivered_order.quantity,
                                                                                 delivered_order.tableID)
        self.__deliveryWaiterArea.setText(delivered_order_output)
