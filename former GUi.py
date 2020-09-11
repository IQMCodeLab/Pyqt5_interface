
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\myself\Groupbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import open_up as op

from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtWidgets import QApplication ,QMainWindow ,QSlider ,QMenu ,QVBoxLayout ,QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import nanonispy as nap
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from scipy import interpolate
from scipy.interpolate import interp1d
from scipy.interpolate import Rbf ,InterpolatedUnivariateSpline
from matplotlib.widgets import Cursor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 922)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.splitter_2)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.splitter_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setSizeIncrement(QtCore.QSize(3, 3))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(4)
        self.splitter.setObjectName("splitter")
        self.verticalLayout.addWidget(self.splitter)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_6 = QtWidgets.QSplitter(self.tab)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.widget = QtWidgets.QWidget(self.splitter_6)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_2.addWidget(self.graphicsView_3)
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label = QtWidgets.QLabel(self.splitter_4)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.label_3.setObjectName("label_3")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.splitter_5)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.splitter_9 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_4 = QtWidgets.QLabel(self.splitter_8)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_8)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_8)
        self.label_6.setObjectName("label_6")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.horizontalSlider = QtWidgets.QSlider(self.splitter_7)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.splitter_7)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.splitter_7)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_4.addWidget(self.splitter_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.splitter_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setMaximum(999)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)

        self.horizontalScrollBar.valueChanged[int].connect(self.changevalue)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
    '''窗口的定义可以参看 GroupBox.ui，这里面有详细参数设定，'''


    def changevalue(self, value):
        self.bias_index = self.horizontalScrollBar.value()
        self.b = op.smooths[0]
        self.bias = self.b[self.bias_index]
        # m=Plotcanvas(self.graphicsView_2,width=10,height=10,bias_index=bias_index)

        self.m2 =PlotPlcaing(self.graphicsView ,width=10 ,height=5 ,bias_index=self.bias_index)
        cid =self.m2.figure.canvas.mpl_connect('button_press_event', self)
        '''这里面的逻辑还是很清楚的，self.m2中的figure.canvas和mpl_connect相连接，也就是我的鼠标是作用在上面的'''
        '''这里我认为后续选点操作问题也不是很大，将之存储起来，这个问题解决起来也不是很难'''
        self.lineEdit_3.setText(str(self.bias))
        self.m2.move(0, 0)

    def __call__(self, event):
        x_data = np.floor(event.xdata)
        self.x_data = x_data.astype(int)
        self.lineEdit.setText(str(self.x_data + 1))
        y_data = np.floor(event.ydata)
        self.y_data = y_data.astype(int)
        self.lineEdit_2.setText(str(self.y_data + 1))
        self.lineEdit_3.setText(str(self.bias))

        m = Plotcanvas(self.graphicsView_3, width=10, height=10, bias_index=self.bias_index)

        self.graphicsView_2.m3 = Plot_2D(self.graphicsView_2, width=8, height=8, xdata=self.x_data, ydata=self.y_data)


class Plot_2D(FigureCanvas):
    def __init__(self, parent=None, width=7, height=7, dpi=100, xdata=1, ydata=1):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.x = op.smooths[0]
        ys = op.smooths[1]
        self.y = ys[xdata, ydata, :]
        self.axs = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(fig)

    def plot(self, fig):
        self.axs.plot(self.x, self.y)
        self.axs.grid(True, linestyle='-.')
        self.axs.tick_params(labelcolor='r', labelsize='medium', width=3)
        self.show()


class Plotcanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=8, dpi=100, bias_index=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.bias_index = bias_index
        self.axs = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  # 这个设定非常的重要，可以确保我最终绘制的图形是在我的graphicsView内的。
        FigureCanvas.setSizePolicy(self, QSizePolicy.Preferred, QSizePolicy.Preferred)
        FigureCanvas.updateGeometry(self)
        self.plot(fig)

    def plot(self, fig):
        lockin_smooth = op.smooths[1]
        interp = 'bilinear'
        self.axs.imshow(lockin_smooth[:, :, self.bias_index], origin='upper', interpolation=interp)
        self.axs.margins(0, 0)
        self.show()


class PlotPlcaing(FigureCanvas):
    def __init__(self, parent=None, width=8, height=8, dpi=100, bias_index=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        self.bias_index = bias_index
        self.axs = self.fig.add_subplot(111)
        self.axs.margins(x=0, y=0, tight=True)
        FigureCanvas.__init__(self, self.fig)  # 使用self和fig来初始化FigureCanvas
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # self.toolbar=NavigationToolbar(self.fig,self)
        self.plot()

    def plot(self):
        lockin_smooth = op.smooths[1]
        self.pcm = self.axs.pcolormesh(lockin_smooth[:, :, self.bias_index], cmap='viridis')
        self.fig.colorbar(self.pcm, ax=self.axs)
        self.cursor = Cursor(self.axs, useblit=True, color='red', linewidth=2)
        self.axs.margins(0)
        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# 傅里叶变换这个近期需要完成
'''
图像上选框放大区域也是需要做的，此外还有一些问题
比如如何设定色度调控条等等，都是需要处理的问题，此外优化一下界面也是很有必要的
并且需要重新写一个open_up.py文件用以处理为进行插值操作的
并且后期对于数据的插值和拟合这也是很重要的
opencv也需要去学习

'''
'''
'''
