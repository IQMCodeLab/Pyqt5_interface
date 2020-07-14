import sys
import matplotlib
from PyQt5 import QtCore
import PyQt5.QtWidgets as QtW
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.widgets import RectangleSelector
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import MouseConnect as ms
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtWidgets import QApplication ,QMainWindow ,QSlider ,QMenu ,QVBoxLayout ,QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
class Ui_Form_impurity(object):
    def setupUi(self, Form, data):
        Form.setObjectName("Form")
        Form.resize(874, 726)
        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap ='binary'
        self.width =8
        self.height=8
        self.dpi=100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.pcolormesh(data,cmap=self.cmap)
        self.canvas.draw()

        self.PTX = []
        self.PTY = []
        self.retranslateUi(Form)
        self.horizontalLayout.addWidget(self.canvas)
        self.fig.canvas.mpl_connect("button_press_event", self.onpress)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def onpress(self,event):
        if event.button==1:
            self.PTX.append([int(event.xdata)])
            self.PTY.append([int(event.ydata)])
            self.ax.scatter(self.PTX,self.PTY)
            self.canvas.draw()
            print("add position:",event.button,event.xdata,event.ydata)
        if event.button==3:
            self.PTX=[]
            self.PTY=[]
            #self.ax.scatter(self.PTX,self.PTY)
            self.canvas.draw()
            print("clear position:",event.button)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



class Ui_Form_bragg(object):
    def setupUi(self, Form, data):
        Form.setObjectName("Form")
        Form.resize(874, 726)
        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap ='binary'
        self.width =8
        self.height=8
        self.dpi=100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.pcolormesh(data,cmap=self.cmap)
        self.canvas.draw()
        self.rs = RectangleSelector(self.ax, self.line_select_callback,
                                    drawtype='line', useblit=True,
                                    button=[1, 3],  # don't use middle button
                                    minspanx=5, minspany=5,
                                    spancoords='pixels',
                                    interactive=True)
        self.retranslateUi(Form)
        self.horizontalLayout.addWidget(self.canvas)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.datas  = dict([('x1',[]),('x2',[]),('y1',[]),('y2',[])])


    def on_click(self, event):
        if event.button == 1 or event.button == 3 and not self.rs.active:
            self.rs.set_active(True)
        else:
            self.rs.set_active(False)

    def line_select_callback(self, eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
        print(" The button you used were: %s %s" % (eclick.button, erelease.button))

        self.datas['x1'].append(int(np.floor(eclick.xdata)))
        self.datas['y1'].append(int(np.floor(eclick.ydata)))
        self.datas['x2'].append(int(np.floor(erelease.xdata)))
        self.datas['y2'].append(int(np.floor(erelease.ydata)))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
