from CustomExceptions.CustomExceptions import *
from Interfaces import Observer
from Interfaces import Subject
from OrderCollection import OrderCollection
from MenuCollection import MenuCollection
from MenuItem import MenuItem
from OrderItem import OrderItem

class Model(object):
    def __init__(self):
        self.__orderCollection = OrderCollection
        self.__menuCollection = MenuCollection
        self.__kitchenList = OrderCollection
        self.__hatchList = set()
        self.__tableOneList = set()
        self.__tableTwoList = set()
        self.__tableThreeList = set()
        self.__tableFourList = set()
        self.__tableFiveList = set()

        self.readFromFile('/Users/lulu/git/FoodOrderSystem/menu_input.txt')

    @property
    def orderCollection(self):
        return self.__orderCollection

    @property
    def menuCollection(self):
        return self.__menuCollection

    def readFromFile(self, fileName):
        try:
            with open(fileName) as inputFile:
                text = inputFile.read()
                newText = text.split('\n')
                for i in range(0, len(newText)):
                    try:
                        self.processLineOfMenu(newText[i])
                        # print('this is text: ', newText[i])
                    except InputLineErrorException as e:
                        logging.error(e.message)
        except FileNotFoundError as e:
            logging.error(e.message)

    def processLineOfMenu(self, line):
        menu = None
        newLine = line.split(',')
        if line(newLine) == 3:
            try:

