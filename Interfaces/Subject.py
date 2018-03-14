from abc import ABCMeta, abstractmethod
from Observer import Observer

# Interface
class Subject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def registerObserver(self, observer): pass

    @abstractmethod
    def removeObserver(self, observer=Observer()): pass

    @abstractmethod
    def notifyObservers(self): pass