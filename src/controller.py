from src.model import Model


class Controller(object):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self):
        """
        Constructor

        """
        self.model = Model()

    def read_csv(self, filename):
        """
        Calls read_csv from model

        :param filename: String Sould be the absolute path to the file
        :return:
        """
        return self.model.read_csv(filename, delimiter=';')

controller = Controller()
