from PyQt5.QtWidgets import *
from Model.Model import Model
from Views.MainActivityGUI import MainActivityGUI
import sys

class Controller:
    def __init__(self, model=Model()):
        self.__model = model
        app = QApplication(sys.argv)
        self.__view = MainActivityGUI(self.__model, self)
        sys.exit(app.exec_())

    def valuechange(self):
        self.__model.speed = self.__view.getselfSpeedControlSlider().value()
