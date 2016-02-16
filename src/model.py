import csv
import os

class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self):
        """
        Constructor

        """
        pass

    def read_csv(self, filename, delimiter=' ', quotechar='|'):
        """
        Reading a .csv file

        :param filename:
        :param delimiter: String Seperation Character which is used in the CSV
        :param quotechar: String
        :return: the csv file as string
        """
        if filename is None:
            raise TypeError("1st parameter was from type None")
        if not filename.endswith('.csv'):
            raise IOError("Wrong file extension, expected file extension was %s, got %s instead" % ('.csv', os.path.splitext(filename)[1]))
        out = ''
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            for row in spamreader:
                out += ', '.join(row)+'\n'
        return out
