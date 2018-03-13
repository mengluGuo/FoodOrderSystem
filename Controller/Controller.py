from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Model.Model import Model
from Views.MainActivityGUI import MainActivityGUI
import sys

class Controller:
    def __init__(self):
        self.__model = Model()
        app = QApplication(sys.argv)
        self.__view = MainActivityGUI(self.__model, self)
        sys.exit(app.exec_())

    def valuechange(self):
        size = self.__view.getselfSpeedControlSlider().value()
        print('size: ',size)


if __name__ == '__main__':
    controler = Controller()