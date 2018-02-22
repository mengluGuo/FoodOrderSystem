from MenuItem import MenuItem

# Items Class stores and manipulates menu item objects.
class MenuCollection:

    # Constructor creates new object and populates set.
    def __init__(self):
        self.__menuCollection = set()

    @property
    def menuCollection(self):
        return self.__menuCollection

    @menuCollection.setter
    def menuCollection(self, menullection = set()):
         self.__menuCollection = menullection

    # Method to add menu in the menu collection
	# @param menu the object of the menu item
    def addMenuItem(self, menu = MenuItem):
        self.__menuCollection.add(menu)