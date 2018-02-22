from CustomExceptions.CustomExceptions import *
import logging

# This is a class constructor of type OrderItem that creates an OrderItem object and sets all its details
# including sequenceID, tableID, dishName and quantity.
# @param String sequenceID is a variable that stores the sequence the OrderItem is served in relevance to other OrderItems.
# @param int tableID is a variable that stores the tableID of the OrderItem.
# @param String dishName a variable that stores the name of the dish served in the OrderItem.
# @param int quantity is a variable that stores the quantity of the ordered dish in this OrderItem.
# @throws IllegalArgumentException and NegativeNumberException
class OrderItem:
    def __init__(self, sequenceID, tableID, dishName, quantity):
        if sequenceID <= 0:
            raise NegativeNumberException('order sequence ID', sequenceID)
        else:
            self.__sequenceID = sequenceID
        if tableID <= 0:
            raise NegativeNumberException('order table ID', tableID)
        else:
            self.__tableID = tableID
        if dishName == '':
            raise EmptyValueException('order dish name', dishName)
        else:
            self.__dishName = dishName
        if quantity <= 0:
            raise NegativeNumberException('order quantity', quantity)
        else:
            self.__quantity = quantity

    @property
    def sequenceID(self):
        return self.__sequenceID

    @sequenceID.setter
    def sequenceID(self, sequenceID):
        self.__sequenceID = sequenceID

    @property
    def tableID(self):
        return self.__tableID

    @tableID.setter
    def tableID(self, tableID):
        self.__tableID = tableID

    @property
    def dishName(self):
        return self.__dishName

    @dishName.setter
    def dishName(self, dishName):
        self.__dishName = dishName

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

# try:
#     menu = OrderItem(0, 0, '', 0)
# except EmptyValueException as e:
#     logging.error(e.message)
# except NegativeNumberException as n:
#     logging.error(n.message)