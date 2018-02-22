import logging

class EmptyValueException(Exception):
    def __init__(self, message):
        logging.basicConfig(format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s', filename='log.log')
        self._log = logging.getLogger(self.__class__.__name__)
        self.message = "Empty value input: " + message

class NegativeNumberException(Exception):
    def __init__(self, place, num):
        logging.basicConfig(format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s', filename='log.log')
        self._log = logging.getLogger(self.__class__.__name__)
        self.message = 'Negative input number for the ' + place + ' : ' + str(num)

class CategoryDoseNotExist(Exception):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s', filename='log.log')
        self._log = logging.getLogger(self.__class__.__name__)
        self.message = 'Category does not exist.'

class TableIDNotFoundException(Exception):
    def __init__(self, tableID):
        logging.basicConfig(format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s', filename='log.log')
        self._log = logging.getLogger(self.__class__.__name__)
        self.message = "The input tableID " + tableID + " doesn't exist."

class InputLineErrorException(Exception):
    def __init__(self, fileName, line):
        logging.basicConfig(format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s', filename='log.log')
        self._log = logging.getLogger(self.__class__.__name__)
        self.message = "Error input line in " + fileName + " file: " + line
