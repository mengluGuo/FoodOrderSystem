from MenuItem import MenuItem

class MenuCollection:

    def __init__(self):
        self.__menuCollection = set()

    @property
    def menuCollection(self):
        return self.__menuCollection

    @menuCollection.setter
    def menuCollection(self, menullection = set()):
         self.__menuCollection = menullection

    def addMenuItem(self, menu = MenuItem):
        self.__menuCollection.add(menu)