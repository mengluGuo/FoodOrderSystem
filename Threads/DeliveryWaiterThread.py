from CustomExceptions.CustomExceptions import *
from Model.Model import Model
from Interfaces.Observer import Observer
from Interfaces.ThreadListener import ThreadListener
import threading
import time


class DeliveryWaiterThread(Observer, threading.Thread):
    def __init__(self, listener=ThreadListener(), model=Model()):
        threading.Thread.__init__(self)
        self.__model = model
        self.__model.registerObserver(self)
        self.runnable = False
        self.__speedUnit = 0.5
        self.__speed = 0
        self.update()
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
                # control the speed of the order waiter thread
                time.sleep(self.__speed)

            if not self.runnable:
                while len(self.__model.getKitchenList()) > 0 or len(self.__model.hatchList) > 0:
                    self.__model.setDeliveredOrder(0)
                    time.sleep(self.__speed)
                self.__listener.changeButtonStatus(False)
                self.__model.resetDeliveryOrder()

    def update(self):
        self.__speed = self.__speedUnit * self.__model.speed
