from abc import ABCMeta, abstractmethod

# Interface
class Subject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def registerObserver(self, observer): pass

    @abstractmethod
    def removeObserver(self, observer): pass

    @abstractmethod
    def notifyObservers(self): pass