from abc import ABCMeta, abstractmethod

# Interface
class ThreadListener(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def changeButtonStatus(self, flag): pass