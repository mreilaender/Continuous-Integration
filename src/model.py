import csv


class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self):
        pass

    def read_csv(self, filename, delimiter=' ', quotechar='|'):
        out = ""
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            for row in spamreader:
                out += ', '.join(row)
        return out
