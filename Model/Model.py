from CustomExceptions.CustomExceptions import *
from Interfaces.Observer import Observer
from Interfaces.Subject import Subject
from OrderCollection import OrderCollection
from MenuCollection import MenuCollection
from MenuItem import MenuItem
from OrderItem import OrderItem
from ReportGenerator import ReportGenerator
import random
import logging


class Model(Subject):
    def __init__(self):
        self.__orderCollection = OrderCollection()
        self.__menuCollection = MenuCollection()
        self.__kitchenList = OrderCollection()
        self.__reportGenerator = ReportGenerator(self.__orderCollection, self.__menuCollection)
        self.__hatchList = list()
        self.__tableOneList = list()
        self.__tableTwoList = list()
        self.__tableThreeList = list()
        self.__tableFourList = list()
        self.__tableFiveList = list()
        self.__registeredObservers = []
        self.__speed = 5
        self.__deliveredOrder = None
        self.__order = None
        self.readFromFile('/Users/lulu/git/FoodOrderSystem/menu_input.txt')

    @property
    def orderCollection(self):
        return self.__orderCollection

    @property
    def menuCollection(self):
        return self.__menuCollection

    @property
    def reportGenerator(self):
        return self.__reportGenerator

    # This is a method to read data from data file
	# @param fileName the file name which the system will read data from
    def readFromFile(self, file_name):
        try:
            with open(file_name) as inputFile:
                text = inputFile.readlines()
                for line in text:
                    try:
                        self.processLineOfMenu(line)
                    except InputLineErrorException as e:
                        logging.error(e.message)
        except FileNotFoundError as e:
            logging.error(e.message)

    # This is a method to write data into a file
    # @param fileName the file name which the system will write data into
    # @param text the data which will be wrote into the file
    def writeIntoFile(self, file_name, text):
        with open(file_name, 'w') as f:
            f.write(text)

    # Method to check the input data, and put into the menu collection
	# @param readingLine a line of data from data file
	# @throws InputLineErrorException
    def processLineOfMenu(self, line):
        menu_obj = line.split(',')
        if len(menu_obj) == 3:
            try:
                menu = MenuItem(menu_obj[0], float(menu_obj[1]), menu_obj[2])
                self.__menuCollection.addMenuItem(menu)
            except EmptyValueException as e:
                logging.error(e.message)
            except NegativeNumberException as e:
                logging.error(e.message)
        else:
            raise InputLineErrorException('menu_input.txt', line)

    @property
    def speed(self):
        return self.__speed

    # Set the speed of Waitress Thread
	# @param time the duration of Thread sleeping
    @speed.setter
    def speed(self, time):
        self.__speed = time
        self.notifyObservers()

    @property
    def order(self):
        return self.__order

    # Method to generate a order randomly, and put this order into kitchen queue
    # @throws NegativeNumberException
    def setRandomOrder(self):
        menu_set = self.menuCollection.menuCollection
        if menu_set and len(menu_set) != 0:
            available_id = self.__orderCollection.findAvailableSequenceID()
            table_id = random.randint(1, 5)
            quantity = random.randint(1, 5)
            order_dictionary = self.__orderCollection.getOrderDictionary()
            # do while loop for avoiding generating orders with duplicated dishes for the same table
            while True:
                menu_id = random.randint(0, len(menu_set) - 1)
                menu = list(menu_set)[menu_id]
                dish_name = menu.dish
                if not (table_id in order_dictionary and dish_name in order_dictionary.get(table_id)):
                    break
            self.__order = OrderItem(available_id, table_id, dish_name, quantity)
            self.__orderCollection.addOrderItem(self.__order)
            self.__kitchenList.addOrderItem(self.__order)
            self.notifyObservers()

    # Method to get kitchen list
	# @return the kitchen list
    def getKitchenList(self):
        return self.__kitchenList.orderList

    # Method to remove the first order item (cooked order) from kitchen list
    # and add the cooked order into the hatch list
    def setHatchList(self, limit):
        if len(self.__kitchenList.orderList) > limit:
            cooked_order = self.__kitchenList.orderList[0]
            self.__kitchenList.orderList.pop(0)
            self.__hatchList.append(cooked_order)
            # notify observers there is a change in the kitchen and hatch list
            self.notifyObservers()

    @property
    def hatchList(self):
        return self.__hatchList

    # Method to remove the first order item from Hatch list
	# and set the Delivered Order equal to the first order item in the hatch list
    def setDeliveredOrder(self, limit):
        if len(self.__hatchList) > limit:
            order = self.__hatchList[0]
            self.__hatchList.pop(0)
            self.__deliveredOrder = order
            self.setTablesOrders()
            self.notifyObservers()

    @property
    def deliveredOrder(self):
        return self.__deliveredOrder

    # Method to take the order item value (Delivered Order)
    # and set it to the corresponding table list
    def setTablesOrders(self):
        if self.__deliveredOrder.tableID == 1:
            self.__tableOneList.append(self.deliveredOrder)
            self.notifyObservers()
        elif self.__deliveredOrder.tableID == 2:
            self.__tableTwoList.append(self.deliveredOrder)
            self.notifyObservers()
        elif self.__deliveredOrder.tableID == 3:
            self.__tableThreeList.append(self.deliveredOrder)
            self.notifyObservers()
        elif self.__deliveredOrder.tableID == 4:
            self.__tableFourList.append(self.deliveredOrder)
            self.notifyObservers()
        elif self.__deliveredOrder.tableID == 5:
            self.__tableFiveList.append(self.deliveredOrder)
            self.notifyObservers()

    @property
    def tableOneList(self):
        return self.__tableOneList

    @property
    def tableTwoList(self):
        return self.__tableTwoList

    @property
    def tableThreeList(self):
        return self.__tableThreeList

    @property
    def tableFourList(self):
        return self.__tableFourList

    @property
    def tableFiveList(self):
        return self.__tableFiveList

    # Method to reset order
    def resetOrder(self):
        self.__order = None
        self.notifyObservers()

    # Method to reset delivery order
    def resetDeliveryOrder(self):
        self.__deliveredOrder = None
        self.notifyObservers()

    """ OBSERVER PATTERN
    SUBJECT must be able to register, remove and notify observers
    self.__registeredObservers: a list to hold any observers"""

    # Method to add an observer object into the observer list
    def registerObserver(self, observer=Observer):
        print (type(observer))

        print('Hello 2: ', observer.__class__)
        if observer not in self.__registeredObservers:
            self.__registeredObservers.append(observer)

    # Method to remove an observer object from the observer list
    def removeObserver(self, observer=Observer):
        self.__registeredObservers.remove(observer)

    # Method to notify related update to registered observers
    def notifyObservers(self):
        for observer in self.__registeredObservers:
            observer.update()

# modle = Model()
# modle.setRandomOrder()