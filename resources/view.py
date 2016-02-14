# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(739, 452)
        self.centralwidget = QtWidgets.QWidget(View)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_area = QtWidgets.QTextEdit(self.centralwidget)
        self.text_area.setObjectName("text_area")
        self.verticalLayout.addWidget(self.text_area)
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setObjectName("open")
        self.verticalLayout.addWidget(self.open)
        View.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(View)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        View.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(View)
        self.statusbar.setObjectName("statusbar")
        View.setStatusBar(self.statusbar)

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "MainWindow"))
        self.open.setText(_translate("View", "Öffnen ..."))

