from Controller.Controller import Controller
from Model.Model import Model

if __name__ == '__main__':
    model = Model()
    controler = Controller(model)

# logging.basicConfig(stream=sys.stdout, format='%(asctime)s -- [%(name)s][%(levelname)s]: %(message)s ', filename=d.LOG_FILE,
# level=logging.DEBUG)
# self._log = logging.getLogger(self.__class__.__name__)