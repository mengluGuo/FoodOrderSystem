from abc import ABCMeta, abstractmethod

# Interface
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self): pass