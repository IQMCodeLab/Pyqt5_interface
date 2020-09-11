import sys
import numpy as np
import binaryfile_read_write as wrb
import open3ds as op
import filops as fp
import read_java_bin
import MouseConnect as ms
from PyQt5 import QtCore, QtGui, QtWidgets
import MouseConnect as mouse
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog,QLineEdit,QAction
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog
#from GUI2 import Ui_Form
import pandas as pg
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import UFiedlCalculation
from GUI_Function_Part import Ui_Form_bragg,Ui_Form_impurity,Ui_Form_Cut
import filops as fp
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout


class Main_windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,800)
        self.initUI()
    def initUI(self):
        centerwidget = self.centralWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(centerwidget)

        self.width=10
        self.height= 10
        self.dpi= 100
        self.figure = Figure(figsize=(self.width,self.height),dpi=self.dpi)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.canvas.draw()
        self.verticalLayout.addWidget(self.canvas)
        self.menuBar =self.menuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.setCentralWidget(centerwidget)


        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setObjectName("graphicsView")


if __name__=="__main__":
    app =QApplication(sys.argv)
    main =Main_windows()
    main.show()
    sys.exit(app.exec_())