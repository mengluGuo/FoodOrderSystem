from CustomExceptions.CustomExceptions import *
from Model.Model import Model
from Interfaces.Observer import Observer
import threading
import time


class OrderWaiterThread(Observer, threading.Thread):
    def __init__(self, model=Model()):
        self.__model = model
        self.__model.registerObserver(self)
        self.update()
        self.runnable = False
        self.__speedUnit = 1000
        self.__speed = 0
        self.__lock = threading.Lock()

    # Method to run the order waiter thread
    def run(self):
        # Ensure once the order waiter thread starts to use an objects's method,
        # other threads cannot use the same method until the order waiter thread is finished.
        with self.__lock:
            while self.runnable:
                if self.__model is not None:
                    try:
                        self.__model.setRandomOrder()
                    except NegativeNumberException as e:
                        logging.error(e.message)
                else:
                    print('self.__model is null')
                # control the speed of the order waiter thread
                time.sleep(self.__speed)
            if not self.runnable:
                self.__model.resetOrder()

    def update(self):
        self.__speed = self.__speedUnit * self.__model.speed

