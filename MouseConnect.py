from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtWidgets import QApplication ,QMainWindow ,QSlider ,QMenu ,QVBoxLayout ,QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.patches import Rectangle



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class Plotcanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=8, dpi=100,topo=[],cmap='binary'):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_tight_layout({'pad':0,'w_pad':0,'h_pad':0})
        fig.set_constrained_layout_pads(w_pad=0, h_pad=0, wspace=0, hspace=0)
        self.cmap =cmap
        self.topo =topo
        self.axs = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  # 这个设定非常的重要，可以确保我最终绘制的图形是在我的graphicsView内的。
        FigureCanvas.setSizePolicy(self, QSizePolicy.Preferred, QSizePolicy.Preferred)
        FigureCanvas.updateGeometry(self)
        self.plot(fig,self.cmap)

    def plot(self, fig,cmap):
        self.axs.pcolormesh(self.topo,cmap=plt.get_cmap(cmap))
        self.show()
class Plotcanvas_With_Mouse(FigureCanvas):
    def __init__(self,parent=None,width=8,height=8,dpi=100,topo=[],cmap='binary'):
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        self.fig.set_tight_layout({'pad':0,'w_pad':0,'h_pad':0})
        self.fig.set_constrained_layout_pads(w_pad=0, h_pad=0, wspace=0, hspace=0)
        self.cmap = cmap
        self.topo = topo
        self.axs =self.fig.add_subplot(111)
        FigureCanvas.__init__(self,self.fig)
        self.axs.pcolormesh(self.topo,cmap=plt.get_cmap(cmap))
        self.rect = Rectangle((0,0),0.2,0.2,color='k',fill=None,alpha=1)
        self.axs.add_patch(self.rect)
        self.rect.set_visible(False)
        self.fig.canvas.draw()
        self.show()

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion )

    def on_click(self,event):
        if event.button ==1 or event.button==3:
            if event.inaxes is not None:
                self.xclick =event.xdata
                self.yclick = event.ydata
                self.onpress = True
    def on_motion(self,event):
        if event.button ==1 or event.button==3 and self.on_press ==True:
            if (self.xclick is not None and self.yclick is not None):
                x0, y0 = self.xclick, self.yclick
                x1, y1 = event.xdata, event.ydata
                if (x1 is not None or y1 is not None):
                    self.rect.set_width(x1 - x0)
                    self.rect.set_height(y1 - y0)
                    self.rect.set_xy((x0, y0))
                    self.rect.set_visible(True)
                    self.draw()  # self.canvas.drawRectangle(self.rect)
class Plotcanvas_with_rect(FigureCanvas):
    def __init__(self,parent=None,width=8,height=8,dpi=100,topo=[],cmap='binary'):
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        self.fig.set_tight_layout({'pad':0,'w_pad':0,'h_pad':0})
        self.fig.set_constrained_layout_pads(w_pad=0, h_pad=0, wspace=0, hspace=0)
        self.cmap = cmap
        self.topo = topo
        self.axs =self.fig.add_subplot(111)
        FigureCanvas.__init__(self,self.fig)
        self.axs.pcolormesh(self.topo,cmap=plt.get_cmap(cmap))
        self.rect = Rectangle((0,0),0.2,0.2,color='k',fill=None,alpha=1)
        self.axs.add_patch(self.rect)
        self.rect.set_visible(False)
        self.fig.canvas.draw()
        self.show()

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion )

    def on_click(self,event):
        if event.button ==1 or event.button==3:
            if event.inaxes is not None:
                self.xclick =event.xdata
                self.yclick = event.ydata
                self.onpress = True
    def on_motion(self,event):
        if event.button ==1 or event.button==3 and self.on_press ==True:
            if (self.xclick is not None and self.yclick is not None):
                x0, y0 = self.xclick, self.yclick
                x1, y1 = event.xdata, event.ydata
                if (x1 is not None or y1 is not None):
                    self.rect.set_width(x1 - x0)
                    self.rect.set_height(y1 - y0)
                    self.rect.set_xy((x0, y0))
                    self.rect.set_visible(True)
                    self.draw()  # self.canvas.drawRectangle(self.rect)