# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/roger/PyQt_eric/demo2/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 555)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 60, 381, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mplvl = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mplvl.setContentsMargins(0, 0, 0, 0)
        self.mplvl.setObjectName("mplvl")
        self.mplwindow = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setObjectName("mplwindow")
        self.mplvl.addWidget(self.mplwindow)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(21, 61, 331, 401))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Explanation_1 = QtWidgets.QLabel(self.widget)
        self.Explanation_1.setObjectName("Explanation_1")
        self.verticalLayout.addWidget(self.Explanation_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.getx = QtWidgets.QLineEdit(self.widget)
        self.getx.setInputMask("")
        self.getx.setObjectName("getx")
        self.horizontalLayout.addWidget(self.getx)
        self.gety = QtWidgets.QLineEdit(self.widget)
        self.gety.setObjectName("gety")
        self.horizontalLayout.addWidget(self.gety)
        self.getz = QtWidgets.QLineEdit(self.widget)
        self.getz.setObjectName("getz")
        self.horizontalLayout.addWidget(self.getz)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnstart = QtWidgets.QPushButton(self.widget)
        self.btnstart.setObjectName("btnstart")
        self.horizontalLayout_2.addWidget(self.btnstart)
        self.btncatch = QtWidgets.QPushButton(self.widget)
        self.btncatch.setObjectName("btncatch")
        self.horizontalLayout_2.addWidget(self.btncatch)
        self.btnbreak = QtWidgets.QPushButton(self.widget)
        self.btnbreak.setObjectName("btnbreak")
        self.horizontalLayout_2.addWidget(self.btnbreak)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "control"))
        self.Explanation_1.setText(_translate("MainWindow", "Give point (x,y,z)"))
        self.label_2.setText(_translate("MainWindow", "Point"))
        self.btnstart.setText(_translate("MainWindow", "start"))
        self.btncatch.setText(_translate("MainWindow", "catch"))
        self.btnbreak.setText(_translate("MainWindow", "break"))
        self.pushButton.setText(_translate("MainWindow", "close system"))
        self.pushButton.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

