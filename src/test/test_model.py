import unittest
import os
from src.model import Model


class TestModel(unittest.TestCase):
    """
    Test cases for src.model

    """
    def setUp(self):
        """
        Sets up the required attributes

        """
        self.model = Model()
        self.resource_path = os.path.abspath('../../resources')

    def tearDown(self):
        """
        Deletes required attributes, before test case is called and before setup is called

        """
        del self.model

    def test_read_csv_none_obj(self):
        """
        Test model.read_csv() with first parameter None

        """
        self.assertRaises(TypeError, self.model.read_csv, None)

    def test_wrong_filetype_no_csv(self):
        """
        Testing model.read_csv() with first parameter being a file with the wrong extension for example .txt or something other than .csv

        """
        self.assertRaises(IOError, self.model.read_csv, self.resource_path + '/gui.ui')
