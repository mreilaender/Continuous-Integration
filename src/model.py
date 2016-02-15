import csv
import os


class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self):
        pass

    def read_csv(self, filename, delimiter=' ', quotechar='|'):
        if filename is None:
            raise TypeError("1st parameter was from type None")
        if not filename.endswith('.csv'):
            raise IOError("Wrong filetype, expected file extension was %s, got %s instead" % ('.csv', os.path.splitext(filename)[1]))
        out = ""
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            for row in spamreader:
                out += ', '.join(row)
        return out
