from Model.Model import Model
from Interfaces.Observer import Observer
import threading
import time


class KitchenThread(Observer, threading.Thread):
    def __init__(self, model=Model()):
        self.__model = model
        self.__model.registerObserver(self)
        self.runnable = False
        self.__speedUnit = 1000
        self.__speed = 0
        self.update()
        self.__lock = threading.Lock()

    # Method to run the order waiter thread
    def run(self):
        # Ensure once the kitchen thread starts to use an objects's method,
        # other threads cannot use the same method until the kitchen thread is finished.
        with self.__lock:
            while self.runnable:
                if self.__model is not None:
                    self.__model.setHatchList(5)
                else:
                    print('self.__model is null')
                # control the speed of the order waiter thread
                time.sleep(self.__speed)
            if not self.runnable:
                while len(self.__model.getKitchenList) > 0:
                    self.__model.setHatchList(0)
                    time.sleep(self.__speed)

    def update(self):
        self.__speed = self.__speedUnit * self.__model.speed

