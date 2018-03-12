# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.controlsVerticalLayout = QtWidgets.QVBoxLayout()
        self.controlsVerticalLayout.setContentsMargins(5, 5, 5, 5)
        self.controlsVerticalLayout.setObjectName("controlsVerticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Library = QtWidgets.QWidget()
        self.Library.setObjectName("Library")
        self.tabWidget.addTab(self.Library, "")
        self.Custom = QtWidgets.QWidget()
        self.Custom.setObjectName("Custom")
        self.listWidget = QtWidgets.QListWidget(self.Custom)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 761, 501))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.Custom, "")
        self.controlsVerticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.controlsVerticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Library), _translate("MainWindow", "Library"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Custom), _translate("MainWindow", "Custom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

