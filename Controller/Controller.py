from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Model.Model import Model
from Views.MainActivityGUI import MainActivityGUI


class Controller(object):
    def __init__(self, model=Model, view=MainActivityGUI):
        self.__model = model
        self.__view = view

class SetListener