# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import numpy as np

from controlCore import couclate, putoff, catch, moveMachineHand

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout

from Ui_main import Ui_MainWindow

'''
class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=10):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,
        QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):
    """动态画布：每秒自动更新，更换一条折线。"""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)
        
    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
        
    def update_figure(self):
        # 构建4个随机整数，位于闭区间[0, 10]
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()
        '''
def testError():
    pass
class MainWindow(QMainWindow, Ui_MainWindow):
    """MainWindow to do"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def addmpl(self, fig):        
        
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        """
        self.mplwindow = QWidget(self)
        #l = QVBoxLayout(self.mplwindow)
        dc = MyDynamicMplCanvas(self.mplwindow, width=5, height=4, dpi=100)
        self.canvas.setParent(self.mplwindow)
        #l.addWidget(dc)
        
        ###force to watch the picture###
        #self.mplwindow.setFocus()
        #self.setCentralWidget(self.mplwindow)
        """
        


    @pyqtSlot()
    def on_btnstart_clicked(self):
        
        x = self.getx.text()
        y = self.gety.text()
        z = self.getz.text()
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            a, b, c = couclate(x, y, z)
            moveMachineHand(a, b, c)
        except:
            print("Error")
        
        
        #print("start", x)
    
    @pyqtSlot()
    def on_btncatch_clicked(self):
        catch()
        print("catch")
    
    @pyqtSlot()
    def on_btnbreak_clicked(self):
        putoff()
        print("break")
        



if __name__=="__main__":

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax1f1.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    #ax1f1.plot(np.random.rand(5))

    app = QApplication(sys.argv)
    dlg  = MainWindow()
    dlg.addmpl(fig1)
    dlg.show()
    sys.exit(app.exec())

