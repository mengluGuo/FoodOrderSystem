from CustomExceptions.CustomExceptions import *
import logging


class MenuItem(object):

    def __init__(self, dish, cost, category):
        if dish == '':
            raise EmptyValueException('menu dish name')
        else:
            self.__dish = dish
        if cost <= 0:
            raise NegativeNumberException('menu dish cost', cost)
        else:
            self.__cost = cost
        if category == '':
            raise EmptyValueException('menu dish category')
        else:
            self.__category = category

    def __eq__(self, other):
        return self.__dish == other.__dish

    def __hash__(self):
        return hash(self.__dish)

    @property
    def dish(self):
        return self.__dish

    @dish.setter
    def dish(self, dish):
        self.__dish = dish

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dish == other.__dish
        return False

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.__dish != other.__dish

"""try:
    menu = MenuItem('KKK', 9, 'ddd')
except EmptyValueException as e:
    logging.error(e.message)
except NegativeNumberException as n:
    logging.error(n.message)"""