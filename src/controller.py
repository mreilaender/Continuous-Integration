import csv
import os

from resources.view import *

import sys
from PyQt5.QtWidgets import *

from src.model import Model


class Controller(QWidget):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_View()
        self.mainwindow = QMainWindow()
        self.model = Model()

        self.view.setupUi(self.mainwindow)
        self.setFixedSize(620, 250)
        self.setup_signals()

    def setup_signals(self):
        # self.view.open.clicked.connect(lambda: self.model.read_file(self.tmp))
        self.view.open.clicked.connect(lambda: self.open_clicked())
        # self.view.pushButton.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton))

    def open_clicked(self):
        fname = QFileDialog.getOpenFileName(self.mainwindow, 'Öffnen ...', os.getcwd())
        csv = self.model.read_csv(fname[0], delimiter=';')
        self.view.text_area.clear()
        self.view.text_area.insertPlainText(csv)


app = QApplication(sys.argv)
controller = Controller()
controller.mainwindow.show()
sys.exit(app.exec_())
