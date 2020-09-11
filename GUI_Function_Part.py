import sys
import matplotlib
from PyQt5 import QtCore
import PyQt5.QtWidgets as QtW
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.widgets import RectangleSelector
from matplotlib.collections import LineCollection
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import MouseConnect as ms

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QInputDialog
from matplotlib.figure import Figure
from matplotlib.ticker import  MultipleLocator,FormatStrFormatter,AutoMinorLocator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtWidgets import QApplication ,QMainWindow ,QSlider ,QMenu ,QVBoxLayout ,QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.patches import Rectangle
import contrast_ratio
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog
from matplotlib.lines import Line2D
from Baseclass import Baseui
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QFileDialog
from javabin import read_java_bin_multi
from mpl_toolkits.mplot3d import Axes3D
import os
#编写一个父类，父类里面包含了图片存储，颜色变换等基本功能
class Ui_Form_impurity(QDialog):
    def __init__(self,data,parent=None):
        super(Ui_Form_impurity,self).__init__()
        #QDialog.__init__(self,parent)
        self.parent = parent
        self.setObjectName("Form")
        self.resize(874, 726)
        self.parent = None
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap ='RdBu'
        self.width =8
        self.height=8
        self.dpi=100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.pcolormesh(self.data,cmap=self.cmap)
        self.ax.axis('off')
        self.canvas.draw()

        self.PTX = []
        self.PTY = []
        self.retranslateUi(self)
        self.horizontalLayout.addWidget(self.canvas)
        self.fig.canvas.mpl_connect("button_press_event", self.onpress)
        QtCore.QMetaObject.connectSlotsByName(self)
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
            self.ax.cla()
            self.ax.pcolormesh(self.data,cmap=self.cmap)
            #self.ax.scatter(self.PTX,self.PTY)
            self.canvas.draw()
            print("clear position:",event.button)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



class Ui_Form_bragg(QDialog):
    def __init__(self,data):
        super(Ui_Form_bragg, self).__init__()
        self.setObjectName("Form")
        self.resize(874, 726)
        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap ='binary'
        self.width =8
        self.height=8
        self.dpi=100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.axis('off')

        self.ax.pcolormesh(data,cmap=self.cmap)
        self.canvas.draw()
        self.rs = RectangleSelector(self.ax, self.line_select_callback,
                                    drawtype='line', useblit=True,
                                    button=[1, 3],  # don't use middle button
                                    minspanx=5, minspany=5,
                                    spancoords='pixels',
                                    interactive=True)
        self.retranslateUi(self)
        self.horizontalLayout.addWidget(self.canvas)

        QtCore.QMetaObject.connectSlotsByName(self)

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



class Ui_Form_Cut(QDialog):
    def __init__(self,data):
        super(Ui_Form_Cut, self).__init__()
        self.setObjectName("Form")
        self.resize(874, 726)
        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap = 'RdBu'
        self.width = 8
        self.height = 8
        self.dpi = 100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.pcolormesh(data, cmap=self.cmap)
        self.canvas.draw()
        self.rect = Rectangle((0,0), 1, 1, facecolor='None', edgecolor='green')
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_motion_event', self.on_motion)
        self.ax.figure.canvas.mpl_connect('button_release_event',self.on_release)
        self.retranslateUi(self)
        self.horizontalLayout.addWidget(self.canvas)
        QtCore.QMetaObject.connectSlotsByName(self)

    def on_press(self, event):
        self.x0 = int(event.xdata)
        self.y0 = int(event.ydata)
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.rect.set_linestyle('dashed')
        self.rect.set_visible(True)

        self.ax.figure.canvas.draw()

    def on_motion(self, event):
        if self.on_press is True:
            return
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.rect.set_linestyle('dashed')
        self.rect.set_visible(True)
        self.ax.figure.canvas.draw()
    def on_release(self, event):
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.rect.set_linestyle('solid')
        self.XPoint =[int(self.x0),int(self.x1)]
        self.YPoint = [int(self.y0),int(self.y1)]
        self.rect.set_visible(True)

        self.ax.figure.canvas.draw()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cut_Figure"))

class Ui_Form_linecut(QDialog):
    def __init__(self,data):
        super(Ui_Form_linecut, self).__init__()
        self.setObjectName("Form")
        self.resize(874, 726)
        self.data = data
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmap = 'RdBu'
        self.width = 8
        self.height = 8
        self.dpi = 100
        self.fig = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.pcolormesh(data, cmap=self.cmap)
        self.ax.axis('off')
        self.font1 = {'family':'Arial',
                      'weight':'normal',
                      'size':22}
        self.ax.tick_params(labelsize=22)
        self.fig.align_xlabels()
        self.canvas.draw()
        self.line = Line2D((0,0),(0,0), color ='red',linewidth=2,linestyle='solid')
        self.ax.add_line(self.line)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_motion_event', self.on_motion)
        self.ax.figure.canvas.mpl_connect('button_release_event',self.on_release)
        self.retranslateUi(self)
        self.horizontalLayout.addWidget(self.canvas)
        QtCore.QMetaObject.connectSlotsByName(self)

    def on_press(self, event):
        self.x0 = int(event.xdata)
        self.y0 = int(event.ydata)
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        #self.line=Line2D((self.x0,self.x1),(self.y0,self.y1),color ='red',linewidth=2,linestyle='solid')

    def on_motion(self, event):
        if self.on_press is True:
            return
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        #self.line=Line2D((self.x0,self.x1),(self.y0,self.y1),color ='red',linewidth=2,linestyle='solid')
    def on_release(self, event):
        self.x1 = int(event.xdata)
        self.y1 = int(event.ydata)
        self.line=Line2D((self.x0,self.x1),(self.y0,self.y1),color ='red',linewidth=2,linestyle='solid')
        self.XPoint =[int(self.x0),int(self.x1)]
        self.YPoint = [int(self.y0),int(self.y1)]
        self.ax.add_line(self.line)
        self.line.set_visible(True)
        self.ax.figure.canvas.draw()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cut_Figure"))
class Ui_Form_didvmap(Baseui):
    def __init__(self,Newbinpath):
        super(Ui_Form_didvmap, self).__init__()
        #Baseui.__init__(self)
        #QWidget.__init__(self)
        self.Newbinpath = Newbinpath

        self.setObjectName("MainWindow")
        self.resize(771, 578)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.canvas)
        self.opendidvmap()
        self.length_z,self.length_y,self.length_x = np.shape(self.didv)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalScrollBar.setMinimum(0)
        self.horizontalScrollBar.setMaximum(self.length_z-1)
        self.horizontalScrollBar.valueChanged.connect(self.topomap_show)
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 20))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.shortcut = QShortcut(QKeySequence('F3'), self.centralwidget, self.changecolor)
        self.shortcut_color_decrease = QShortcut(QKeySequence('F2'),self.centralwidget,self.changecolor_decrease)
        self.shortcut_1 = QShortcut(QKeySequence('Ctrl+Q'), self.centralwidget, self.dialog_open)
        self.shortcut_2 = QShortcut(QKeySequence('Ctrl+S'), self.centralwidget, self.savepng)
        self.shortcut_3 = QShortcut(QKeySequence('Ctrl+B'), self.centralwidget, self.savedata_bin)
        self.shortcut_4 = QShortcut(QKeySequence('F11'), self.centralwidget, self.contrast_ratio)
        self.shortcut_5 = QShortcut(QKeySequence('Ctrl+L'),self.centralwidget,self.linecut)
#        self.shortcut_6 = QShortcut(QKeySequence('Ctrl+F'),self.centralwidget,self.fourier_transform)
        self.shortclipboard = QShortcut(QKeySequence('Ctrl+C'),self.centralwidget,self.to_clipboard)
        self.shortcutLinecut = QShortcut(QKeySequence('Shift+L'),self.centralwidget,self.shiftlinecut)
        #self.shortcut3dlinecut = QShortcut(QKeySequence('Shift+D'),self.centralwidget,self.s3dlinecut)
        QtCore.QMetaObject.connectSlotsByName(self)

    """
    def fourier_transform(self):
    """

    def opendidvmap(self):
        print("nihao")
        self.filename,_ = QFileDialog.getOpenFileName(self.centralwidget,'openfile','C:\\data','binfile(*.bin)')
        self.Newbinpath,self.dirmap = os.path.split(self.filename)
        self.didv,self.biaslist = read_java_bin_multi(self.filename)
        print(self.biaslist)


    def topomap_show(self):
        self.nowlayer = self.horizontalScrollBar.value()
        self.topo = self.didv[self.nowlayer,:,:]
        self.nowbias = self.biaslist[self.nowlayer]
        self.topomap_draw(self.topo)

    def savepng(self):
        self.counts =self.counts +1
        self.ax.axis('off')
        self.figure.savefig(self.Newbinpath+'\\'+'didvmap'+'_'+str(self.nowbias)+'.eps',dpi=100,format='eps')
        self.figure.savefig(self.Newbinpath+'\\'+'didvmap'+'_'+str(self.nowbias)+'.png',dpi=600,format='png')
        self.ax.axis('on')

    def linecut(self):
        self.windows_1 = Ui_Form_linecut(self.topo)
        self.windows_1.exec_()
        self.x = self.windows_1.XPoint
        self.y = self.windows_1.YPoint

        self.xpointlist =np.linspace(self.x[0],self.x[1],np.abs(self.x[1]-self.x[0])+1,dtype=int)
        self.ypointlist =np.trunc(self.y[0] + ((self.y[1]-self.y[0])/(self.x[1]-self.x[0]))*(self.xpointlist-self.x[0]))
        self.ypointlist = self.ypointlist.astype(int)
        """
        这里写的不好看
        """
        self.length_xpoint = len(self.xpointlist)
        self.didvlist = np.zeros((self.length_z,self.length_xpoint))
        for i in range(self.length_xpoint):
            y = self.ypointlist[i]
            x = self.xpointlist[i]
            self.didvlist[:,i] =  self.didv[:,y,x]
        self.windows_2 = didvlistwindows(self.didvlist,self.biaslist,self.Newbinpath)
        self.windows_2.show()
    """
    def s3dlinecut(self):
        self.windows_1 = Ui_Form_linecut(self.topo)
        self.windows_1.exec_()
        self.x = self.windows_1.XPoint
        self.y = self.windows_1.YPoint

        self.xpointlist =np.linspace(self.x[0],self.x[1],np.abs(self.x[1]-self.x[0])+1,dtype=int)
        self.ypointlist =np.trunc(self.y[0] + ((self.y[1]-self.y[0])/(self.x[1]-self.x[0]))*(self.xpointlist-self.x[0]))
        self.ypointlist = self.ypointlist.astype(int)
        
        #这里写的不好看
    
        self.length_xpoint = len(self.xpointlist)
        self.didvlist = np.zeros((self.length_z,self.length_xpoint))
        for i in range(self.length_xpoint):
            y = self.ypointlist[i]
            x = self.xpointlist[i]
            self.didvlist[:,i] =  self.didv[:,y,x]
        self.windows_2 = threeDimenlistwindows(self.didvlist,self.biaslist,self.Newbinpath)
        self.windows_2.show()
    """


    def shiftlinecut(self):
        self.windows_1 = Ui_Form_linecut(self.topo)
        self.windows_1.exec_()
        self.x = self.windows_1.XPoint
        self.y = self.windows_1.YPoint

        self.xpointlist =np.linspace(self.x[0],self.x[1],np.abs(self.x[1]-self.x[0])+1,dtype=int)
        self.ypointlist =np.trunc(self.y[0] + ((self.y[1]-self.y[0])/(self.x[1]-self.x[0]))*(self.xpointlist-self.x[0]))
        self.ypointlist = self.ypointlist.astype(int)
        """
        这里写的不好看
        """
        self.length_xpoint = len(self.xpointlist)
        self.didvlists = np.zeros((self.length_z,self.length_xpoint))
        for i in range(self.length_xpoint):
            y = self.ypointlist[i]
            x = self.xpointlist[i]
            self.didvlists[:,i] =  self.didv[:,y,x]
        text, ok = QInputDialog.getInt(self.centralwidget, 'dialog', '输入你想要展现在Linecut里面的点数')
        if ok:
            self.pointnumber = int(text)
        self.interval = self.length_xpoint//self.pointnumber
        self.didvlist = np.zeros((self.length_z,self.pointnumber))
        for i in range(self.pointnumber):
            y = self.ypointlist[i*self.interval]
            x = self.xpointlist[i*self.interval]
            self.didvlist[:, i] = self.didv[:, y, x]
        self.ax.scatter(self.xpointlist,self.ypointlist,color='black')
        self.canvas.draw()
        self.windows_3 = linecutshow(self.didvlist.T,self.biaslist,self.Newbinpath)
        self.windows_3.show()


        
class linecutshow(Baseui):
    def __init__(self,data,biaslist,Newbinpath):
        super(linecutshow, self).__init__()

        self.topos = data
        self.topo = []
        self.width = np.shape(self.topos)[1]/10
        self.height = np.shape(self.topos)[0]/10
        self.offset = np.abs(np.min(self.topos))/10
        self.biaslist = biaslist
        self.Newbinpath = Newbinpath
        self.length = np.shape(self.topos)[0]
        for i in range(self.length):
            a = self.topos[i,:]+self.offset*i
            #a =self.topos[i,:]
            self.topo.append(a)
        self.width = 12
        self.height = 16
        self.ax.axis('on')
        self.ax = self.figure.gca()
        self.bwitch = 2
        self.font = {'family': 'Arial', 'weight': 'normal', 'size': 30, }
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)
        self.ax.tick_params(which='minor', direction='in', length=6, width=2, labelsize=22, axis='both')
        self.ax.tick_params(which='major', direction='in', length=12, width=2, labelsize=22)
        self.ax.set_xlabel('Bias (V)',self.font)
        self.majorLocation_x = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/5)
        self.minorLocation_x = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/10)
        self.ax.xaxis.set_major_locator(self.majorLocation_x)
        self.ax.xaxis.set_minor_locator(self.minorLocation_x)
        self.ax.set_yticks([])
        #self.ax.xticks(fontproperties='Arial', size=22)
        self.line_segments = LineCollection([np.column_stack([self.biaslist,y]) for y in self.topo],
                                            linewidths=(2),linestyles='solid',cmap=self.cmap)
        self.line_segments.set_array(self.biaslist)
        self.ax.add_collection(self.line_segments)
        self.ax.set_xlim(np.min(self.biaslist)-(np.max(self.biaslist)-np.min(self.biaslist))/20,np.max(self.biaslist)+(np.max(self.biaslist)-np.min(self.biaslist))/20)
        self.ax.set_ylim(np.min(self.topo)-self.offset,np.max(self.topo)+self.offset)
        self.canvas.draw()
        #self.ax.yticks(fontproperties='Arial', size=22)
        #self.ax.set_xlabel('Location (m)', self.font)
        #self.ax.set_ylabel('dI/dV (a.u)', self.font)

        #self.index_X, self.index_Y = np.meshgrid(self.length, self.biaslist)
        #self.ax.pcolormesh(self.index_X, self.index_Y, self.topo, cmap=self.cmap)
        self.horizontalLayout.addWidget(self.canvas)
        #self.shortcut_4 = QShortcut(QKeySequence('F11'),self.centralwidget,self.contrast_ratio)

    def contrast_ratio(self):
        print("nihao")
        self.max = np.max(self.topo)
        self.min = np.min(self.topo)
        self.median = np.median(self.topo)
        self.windows_c = contrast_ratio.Ui_Form_Contrast_single()
        self.windows_c.slider_emit.connect(self.sliderfunction)
        # self.windows.slider_2_emit.connect(self.slidernumber2)
        self.windows_c.show()
    def sliderfunction(self,number1):
        self.topo = []
        for i in range(self.length):
            a = self.topos[i,:]+self.offset*i*number1/50
            #a =self.topos[i,:]
            self.topo.append(a)
        self.topomap_draw(self.topo)
    def savepng(self):
        self.counts = self.counts + 1
        self.ax.axis('on')
        self.figure.savefig(self.Newbinpath + '\\' + 'didvlinecut' + '_' + str(self.counts) + '.eps', dpi=100,
                            format='eps')
        self.figure.savefig(self.Newbinpath + '\\' + 'didvlinecut' + '_' + str(self.counts) + '.png', dpi=600,
                            format='png')

    def topomap_draw(self,data,vmin=0,vmax=100):
        print(vmin,vmax)
        self.vmin = np.percentile(data,vmin)
        self.vmax = np.percentile(data,vmax)
        self.ax.clear()
        self.ax.axis('on')
        self.ax = self.figure.gca()
        self.bwitch = 2
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)
        self.ax.tick_params(which='minor', direction='in', length=6, width=2, labelsize=22, axis='both')
        self.ax.tick_params(which='major', direction='in', length=12, width=2, labelsize=22)
        self.ax.set_xlabel('Bias (V)',self.font)
        self.majorLocation_x = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/5)
        self.minorLocation_x = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/10)
        self.ax.xaxis.set_major_locator(self.majorLocation_x)
        self.ax.xaxis.set_minor_locator(self.minorLocation_x)
        self.ax.set_yticks([])
        #self.ax.pcolormesh(data,vmin = self.vmin,vmax=self.vmax,cmap=plt.get_cmap(self.cmap))
        #self.ax.pcolormesh(data, vmin=self.vmin, vmax=self.vmax, cmap=self.cmap)
        self.line_segments = LineCollection([np.column_stack([self.biaslist,y]) for y in data], linewidths=(2),linestyles='solid',cmap=self.cmap)
        self.line_segments.set_array(self.biaslist)
        self.ax.add_collection(self.line_segments)
        self.ax.set_xlim(np.min(self.biaslist),np.max(self.biaslist))
        self.ax.set_ylim(np.min(data)-self.offset/5,np.max(data)+self.offset/5)
        self.canvas.draw()
"""
class threeDimenlistwindows(Baseui):
    def __init__(self,data,biaslist,Newbinpath):
        super(threeDimenlistwindows, self).__init__()

        self.topo = data
        self.biaslist = biaslist
        self.Newbinpath = Newbinpath
        self.offset = np.abs(np.max(self.topo))

        length = np.shape(self.topo)[1]
        self.Y =np.linspace(1,length,length,dtype=int)
        self.width =10
        self.height = 10
        self.figure = Figure(figsize=(self.width, self.height), dpi=self.dpi)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.gca(projection='3d')
        self.ax.axis('on')
        self.bwitch = 2
        self.font = {'family': 'Arial', 'weight': 'normal', 'size': 30, }
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)
        self.ax.tick_params(which='both', axis='both', direction='in', width=2, labelsize=22)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()+self.ax.get_zticklabels()
        [label.set_fontname('Arial') for label in labels]
        # self.ax.xticks(fontproperties = 'Arial',size=22)
        # self.ax.yticks(fontproperties = 'Arial',size=22)
        self.ax.set_ylabel('Location (m)', self.font)
        self.ax.set_xlabel('Bias (V)', self.font)
        self.ax.set_yticks([])
        self.x,self.y= np.meshgrid(self.Y,self.biaslist)
        self.ax.set_xlim(np.min(self.x),np.max(self.x))
        self.ax.set_zlim(np.min(self.topo)-self.offset,np.max(self.topo)+self.offset)
        self.ax.plot_surface(self.x, self.y, data,cmap=self.cmap)
        self.canvas.draw()
    def topomap_draw(self,data,vmin=0,vmax=100):
        print(vmin,vmax)
        self.vmin = np.percentile(data,vmin)
        self.vmax = np.percentile(data,vmax)
        self.ax = self.figure.gca(projection='3d')
        self.ax.axis('on')
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)
        self.ax.tick_params(which='both', axis='both', direction='in', width=2, labelsize=22)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname('Arial') for label in labels]
        # self.ax.xticks(fontproperties = 'Arial',size=22)
        # self.ax.yticks(fontproperties = 'Arial',size=22)
        self.ax.set_ylabel('Location (m)', self.font)
        self.ax.set_xlabel('Bias (V)', self.font)
        self.ax.set_zyticks([])
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()+self.ax.get_zticklabels()
        [label.set_fontname('Arial') for label in labels]

        self.ax.set_xlim(np.min(self.x),np.max(self.x))
        self.ax.set_zlim(np.min(self.topo)-self.offset,np.max(self.topo)+self.offset)
        self.ax.plot_surface(self.x, self.y, data,vmin=self.vmin,vmax=self.vmax,cmap=self.cmap)
        self.canvas.draw()
"""


class didvlistwindows(Baseui):
    def __init__(self,data,biaslist,Newbinpath):
        super(didvlistwindows, self).__init__()

        self.topo = data
        print(np.shape(self.topo))
        self.biaslist = biaslist
        self.Newbinpath = Newbinpath
        length = np.shape(self.topo)[1]
        self.width = np.shape(self.topo)[1]/10
        self.height = np.shape(self.topo)[0]/10
        self.ax.axis('on')
        self.ax = self.figure.gca()
        self.bwitch =2
        self.font = {'family' : 'Arial','weight' : 'normal','size': 30,}
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)
        self.length = np.linspace(1,length,length)

        self.majorLocation_y = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/5)
        self.minorLocation_y = MultipleLocator((np.max(self.biaslist)-np.min(self.biaslist))/10)
        self.majorLocation_x = MultipleLocator((np.max(self.length) - np.min(self.length)) / 5)

        self.ax.xaxis.set_major_locator(self.majorLocation_x)
        self.ax.yaxis.set_major_locator(self.majorLocation_y)
        self.ax.yaxis.set_minor_locator(self.minorLocation_y)
        self.ax.tick_params(which='both',axis='both',direction='in',width=2,labelsize=22)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname('Arial') for label in labels]
        #self.ax.xticks(fontproperties = 'Arial',size=22)
        #self.ax.yticks(fontproperties = 'Arial',size=22)
        self.ax.set_xlabel('Location (m)',self.font)
        self.ax.set_ylabel('Bias (V)',self.font)
        self.index_X,self.index_Y = np.meshgrid(self.length,self.biaslist)
        self.ax.pcolormesh(self.index_X,self.index_Y,self.topo,cmap=self.cmap)
        self.horizontalLayout.addWidget(self.canvas)

    def savepng(self):
        self.counts =self.counts +1
        self.ax.axis('on')
        self.figure.savefig(self.Newbinpath+'\\'+'didvlistmap'+'_'+str(self.counts)+'.eps',dpi=100,format='eps')
        self.figure.savefig(self.Newbinpath+'\\'+'didvlistmap'+'_'+str(self.counts)+'.png',dpi=600,format='png')
    def topomap_draw(self,data,vmin=0,vmax=100):
        self.vmin = np.percentile(data,vmin)
        self.vmax = np.percentile(data,vmax)
        self.ax.clear()
        self.ax.axis('on')
        self.ax = self.figure.gca()
        self.bwitch =2
        self.ax.spines['top'].set_linewidth(self.bwitch)
        self.ax.spines['left'].set_linewidth(self.bwitch)
        self.ax.spines['right'].set_linewidth(self.bwitch)
        self.ax.spines['bottom'].set_linewidth(self.bwitch)

        self.majorLocation_y = MultipleLocator((np.max(self.biaslist) - np.min(self.biaslist)) / 5)
        self.minorLocation_y = MultipleLocator((np.max(self.biaslist) - np.min(self.biaslist)) / 10)
        self.majorLocation_x = MultipleLocator((np.max(self.length) - np.min(self.length)) / 5)

        self.ax.xaxis.set_major_locator(self.majorLocation_x)
        self.ax.yaxis.set_major_locator(self.majorLocation_y)
        self.ax.yaxis.set_minor_locator(self.minorLocation_y)


        self.ax.tick_params(which='both',axis='both',direction='in',width=2,labelsize=22)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname('Arial') for label in labels]
        #self.ax.xticks(fontproperties = 'Arial',size=22)
        #self.ax.yticks(fontproperties = 'Arial',size=22)
        self.ax.set_xlabel('Location (m)',self.font)
        self.ax.set_ylabel('Bias (V)',self.font)
        #self.ax.pcolormesh(data,vmin = self.vmin,vmax=self.vmax,cmap=plt.get_cmap(self.cmap))
        self.ax.pcolormesh(self.index_X,self.index_Y,data,vmin=self.vmin,vmax=self.vmax,cmap=self.cmap)
        self.canvas.draw()


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Newbin =  r'C:\data'
    ui = Ui_Form_didvmap(Newbin)
    ui.show()
    sys.exit(app.exec_())