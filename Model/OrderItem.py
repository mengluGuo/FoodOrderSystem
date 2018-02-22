class OrderItem:

    def __init__(self, sequenceID, tableID, dishName, quantity):
        self.__sequenceID = sequenceID
        self.__tableID = tableID
        self.__dishName = dishName
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
