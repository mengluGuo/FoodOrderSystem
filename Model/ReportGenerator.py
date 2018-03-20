from Model.MenuCollection import MenuCollection
from Model.OrderCollection import OrderCollection
from CustomExceptions.CustomExceptions import *


class ReportGenerator(object):
    def __init__(self, order_collection=OrderCollection, menu_collection=MenuCollection):
        self.__orderCollection = order_collection
        self.__menuCollection = menu_collection
        self.__space = '  '

    # Method to get the frequency report
    # @return output the String of frequency report
    def getFrequencyReport(self):
        output = '\n\nFREQUENCY REPORT\n================\n'
        frequency_dictionary = self.__orderCollection.getFrequencyDictionary()
        for key, value in frequency_dictionary.items():
            if key is not None:
                dish_name = key
                quantity = value
                output += '%20s' % dish_name + str(quantity) + '\n'
        return output

    # Method to get the not ordered dishes
    # @return output the String of not ordered dishes
    def getDishesNotOrder(self):
        output = '\n\nDISHES NOT ORDERED\n==================\n'
        menu_collection = self.__menuCollection.getMenuCollection()
        for menu in menu_collection:
            dish_name = menu.dish
            frequency_dictionary = self.__orderCollection.getFrequencyDictionary()
            # if frequency_dictionary[dish_name] is not None:
            if dish_name in frequency_dictionary:
                output += dish_name + '\n'
        return output

    # Read menu input file and to hold the category, dish name and price for
    # all menu item and return these in concatenated string.
    # @return output the string of menu list
    def getMenuList(self):
        output = '\n MENU\n=====\n\nSTARTER\n' + self.listStarters() \
                 + '\nMAIN\n' + self.listMains() \
                 + '\nDESSERT\n' + self.listDesserts() \
                 + '\nDRINKS\n' + self.listDrinks()
        return output

    # Read details of Starters items from menu input file.
    # @return output the string of the starter list
    def listStarters(self):
        output = ''
        menu_collection = self.__menuCollection.getMenuCollection()
        for menu in menu_collection:
            if 'starter' in menu.category:
                output += self.__space + '%15s' % menu.dish + '%.2f' % str(menu.cost) + '\n'
        return output

    # Read details of Mains items from menu input file.
    # @return output the string of the main list
    def listMains(self):
        output = ''
        menu_collection = self.__menuCollection.getMenuCollection()
        for menu in menu_collection:
            if 'main' in menu.category:
                output += self.__space + '%15s' % menu.dish + '%.2f' % str(menu.cost) + '\n'
        return output

    # Read details of Desserts items from menu input file.
    # @return output the string of the dessert list
    def listDesserts(self):
        output = ''
        menu_collection = self.__menuCollection.getMenuCollection()
        for menu in menu_collection:
            if 'dessert' in menu.category:
                output += self.__space + '%15s' % menu.dish + '%.2f' % str(menu.cost) + '\n'
        return output

    # Read details of Drinks items from menu input file.
    # @return output the string of the drink list
    def listDrinks(self):
        output = ''
        menu_collection = self.__menuCollection.getMenuCollection()
        for menu in menu_collection:
            if 'drink' in menu.category:
                output += self.__space + '%15s' % menu.dish + '%.2f' % str(menu.cost) + '\n'
        return output

    # Method to get the summary of all tables
    # @return output the String of all tables' summary
    def getTablesSummary(self):
        output = 'TABLE SUMMARY\n============='
        order_dictionary = self.__orderCollection.getOrderDictionary()
        for key, value in order_dictionary.items():
            if key is not None:
                output += str(self.getBillByTableID(key))
        return output

    # Method to get bill by table id
    # @param tableID the input table id
    # @return output the string of bill
    def getBillByTableID(self, tableID):
        order_dictionary = self.__orderCollection.getOrderDictionary()
        if tableID < 0:
            raise NegativeNumberException('table ID', tableID)
        elif tableID not in order_dictionary:
            raise TableIDNotFoundException(tableID)
        else:
            dish_name = ''
            quantity = 0
            sum_price = self.getSumPrice(tableID)
            discount = self.getDiscount(sum_price)
            discounted_price = self.getDiscountedPrice(sum_price, discount)
            output = '\nTABLE' + str(tableID) + '\n'
            order_dictionary = self.__orderCollection.getOrderDictionary()
            dish_dictionary = order_dictionary[tableID]
            for key, value in dish_dictionary.items():
                if key is not None:
                    dish_name = key
                    quantity = value
                    for menu in self.__menuCollection.getMenuCollection():
                        if menu.dish == dish_name:
                            per_dish_price = menu.cost
                total_dish_price = per_dish_price * quantity
                output += '%15s' % dish_name + '%2s' % str(quantity) \
                            + '%2s' % '*' + '%2s' % str(per_dish_price) \
                            + ' = ' + str(total_dish_price) + '\n'
            output += '\n====\n' + '%10s' % 'Total for this table: ' + str(sum_price) + '\n' \
                        + '%23s' % 'Discount: ' + str(discount) + '\n' \
                        + '%23s' % 'Total after Discount: ' + str(discounted_price) + '\n'
            return output

    # Method to get the sum price by table id
    # @param tableID the input table id
    # @return sum_price
    def getSumPrice(self, table_id):
        sum_price = 0
        order_dictionary = self.__orderCollection.getOrderDictionary()
        menu_dictionary = self.__menuCollection.getMenuCollection()
        if order_dictionary[table_id] is not None:
            for key, value in order_dictionary.items():
                if key is not None:
                    dish_name = key
                    quantity = value
                    for menu in menu_dictionary:
                        if menu.dish == dish_name:
                            sum_price += menu.cost * quantity
        return sum_price

    # Method to get the discount of a table which the sum price is over 30
    # @param sum_price the sum price of a table
    # @return the discount
    def getDiscount(self, sum_price):
        discount_rate = 0.15
        discount = 0
        if sum_price > 30:
            discount = sum_price * discount_rate
        return discount

    # Method to get the final price after discount
    # @param sum_price the sum price of a table
    # @param discount the discount of a table
    # @return the final price of a table
    def getDiscountedPrice(self, sum_price, discount):
        discounted_price = sum_price - discount
        return discounted_price

    # Method to get the final report
    # @return the string of the final report
    def getFinalReport(self):
        output = self.getTablesSummary() + self.getFrequencyReport() + self.getDishesNotOrder() + self.getMenuList()
        return output
