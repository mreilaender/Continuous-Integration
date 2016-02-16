from src.model import Model
from nose.tools import assert_raises
from nose import with_setup
import nose


class TestCSV:
    def mysetup(self):
        print("asd")
        self.model = Model()

    def myteardown(self):
        del self.model

    @with_setup(mysetup, myteardown)
    def test_asd(self):
        assert_raises(IOError, self.model.read_csv, "..\\resources\\gui.ui")
