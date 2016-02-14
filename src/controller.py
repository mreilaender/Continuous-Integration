from src.model import Model


class Controller(object):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self):
        self.model = Model()

    def read_csv(self, filename):
        return self.model.read_csv(filename, delimiter=';')

controller = Controller()
csv = controller.model.read_csv("..\\resources\\sample.csv")
# print(csv)
