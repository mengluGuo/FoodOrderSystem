from OrderItem import OrderItem

class OrderCollection:

    __currentSequenceID = 0

    def __init__(self):
        self.__orderList = list()

    @property
    def orderList(self):
        return self.__orderList

    @orderList.setter
    def orderList(self, orderList = list()):
        self.__orderList = orderList

    def addOrderItem(self, order = OrderItem):
        self.__currentSequenceID = order.sequenceID
        self.__orderList.append(order)

    def getOrderDictionary(self):
        orderDict = dict()
        for order in self.__orderList:
            tableID = order.tableID
            if tableID in orderDict.keys():
                dishDict = orderDict[tableID]
                dishDict[order.dishName] = order.quantity
            else:
                dishDict = dict()
                dishDict[order.dishName] = order.quantity
                orderDict[tableID] = dishDict
        return orderDict

    def getFrequencyDictionary(self):
        frequencyDict = dict()
        for order in self.__orderList:
            dishName = order.dishName
            dishQuantity = order.quantity
            if dishName in frequencyDict.keys():
                oldQuantity = frequencyDict[dishName]
                newQuantity = oldQuantity + dishQuantity
                frequencyDict[dishName] = newQuantity
            else:
                frequencyDict[dishName] = dishQuantity
        return frequencyDict

    def findAvailableSequenceID(self):
        return self.__currentSequenceID + 1

"""order1 = OrderItem(1, 1, 'Fish and Chips', 2)
order2 = OrderItem(2, 1, 'KongPao Chicken', 3)
order3 = OrderItem(3, 1, 'Pasta', 4)
order4 = OrderItem(4, 2, 'Fish and Chips', 3)
order5 = OrderItem(5, 2, 'KongPao Chicken', 4)
order6 = OrderItem(6, 2, 'Pasta', 5)
orderCollection1 = OrderCollection()
orderCollection1.addOrderItem(order1)
orderCollection1.addOrderItem(order2)
orderCollection1.addOrderItem(order3)
orderCollection1.addOrderItem(order4)
orderCollection1.addOrderItem(order5)
orderCollection1.addOrderItem(order6)
print orderCollection1.getOrderDictionary()
print orderCollection1.getFrequencyDictionary()"""