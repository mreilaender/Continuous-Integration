import unittest
import os
from src.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.resource_path = os.path.abspath('../../resources')

    def tearDown(self):
        del self.model

    def test_read_csv_none_obj(self):
        self.assertRaises(TypeError, self.model.read_csv, None)

    def test_wrong_filetype_no_csv(self):
        self.assertRaises(IOError, self.model.read_csv, self.resource_path + '/gui.ui')
