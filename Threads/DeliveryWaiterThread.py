from CustomExceptions.CustomExceptions import *
from Model.Model import Model
from Interfaces.Observer import Observer
from Interfaces.ThreadListener import ThreadListener
import threading
import time


class KitchenThread(Observer, threading.Thread):
    def __init__(self,listener = ThreadListener(), model=Model()):
        self.__model = model
        self.__model.registerObserver(self)
        self.update()
        self.runnable = False
        self.__speedUnit = 800
        self.__speed = 0
        self.__lock = threading.Lock()
        self.__listener = listener

    # Method to run the order waiter thread
    def run(self):
        # Ensure once the delivery waiter thread starts to use an objects's method,
        # other threads cannot use the same method until the delivery waiter thread is finished.
        with self.__lock:
            while self.runnable:
                if self.__model is not None:
                    self.__model.setDeliveredOrder(3)
                else:
                    print('self.__model is null')
                # control the speed of the order waiter thread
                time.sleep(self.__speed)
            if not self.runnable:
                while len(self.__model.getKitchenList) > 0 and len(self.__model.hatchList) > 0:
                    self.__model.setDeliveredOrder(0)
                    time.sleep(self.__speed)
                self.__listener.changeButtonStatus(True)
                self.__model.resetDeliveryOrder()

    def update(self):
        self.__speed = self.__speedUnit * self.__model.speed