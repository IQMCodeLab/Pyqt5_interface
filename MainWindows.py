
#code by ping
#9/5/2020

import binaryfile_read_write as wrb
import open3ds as op
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QFileDialog,QShortcut
from PyQt5.QtGui import QKeySequence
import UFiedlCalculation
import filops as fp
import javabin
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from subtract_fit import *

from GUI_Function_Part import Ui_Form_bragg, Ui_Form_impurity, Ui_Form_Cut, Ui_Form_didvmap
from Baseclass import Baseui

class Ui_MainWindow(Baseui):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(805, 709)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.fft_count = 0
        self.count_bin = 0

        self.verticalLayout.addWidget(self.canvas)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("drift_correction")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("图形处理")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName('绘制linecut')


        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionchoose_color = QtWidgets.QAction(self)
        self.actionchoose_color.setObjectName("actionchoose_color")

        self.actionopen3ds = QtWidgets.QAction(self)
        self.actionopen3ds.setObjectName("actionopen3ds")
        self.actionopen3ds.setShortcut('Shift+D')

        self.actionopenpythonbin = QtWidgets.QAction(self)
        self.actionopenpythonbin.setObjectName("actionopenpythonbin")
        self.actionopenpythonbin.setShortcut('Shift+p')

        self.actionopenjavabin = QtWidgets.QAction(self)
        self.actionopenjavabin.setObjectName("actionopenjavabin")
        self.actionopenjavabin.setShortcut('Shift+j')

        self.actionopendidvdata = QtWidgets.QAction(self)
        self.actionopendidvdata.setObjectName('actionopendidvdat')
        self.actionopendidvdata.setShortcut('shift+d')


        self.actionochooseimpurities = QtWidgets.QAction(self)
        self.actionochooseimpurities.setObjectName("choose_impurities")
        self.actionoaddmask = QtWidgets.QAction(self)
        self.actionoaddmask.setObjectName("add_mask")

        self.actionochooseBraggPeak = QtWidgets.QAction(self)
        self.actionochooseBraggPeak.setObjectName("chooseBraggPeak")
        self.actionoDoingDrfitCorrection=QtWidgets.QAction(self)
        self.actionoDoingDrfitCorrection.setObjectName("DriftCorrection")

        self.actioncutfigure =QtWidgets.QAction(self)
        self.actioncutfigure.setObjectName("cutfigure")

        self.actiondidvs = QtWidgets.QAction(self)
        self.actiondidvs.setObjectName('didvmap')

        self.menu.addAction(self.actionopen3ds)
        self.menu.addAction(self.actionopenpythonbin)
        self.menu.addAction(self.actionopenjavabin)
        self.menu.addAction(self.actionopendidvdata)

        self.menu_2.addAction(self.actionchoose_color)

        self.menu_3.addAction(self.actionochooseimpurities)
        self.menu_3.addAction(self.actionoaddmask)

        self.menu_4.addAction(self.actionochooseBraggPeak)
        self.menu_4.addAction(self.actionoDoingDrfitCorrection)

        self.menu_5.addAction(self.actioncutfigure)

        self.menu_6.addAction(self.actiondidvs)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())



        self.actionchoose_color.triggered.connect(self.choosecolor)
        self.actionopen3ds.triggered.connect(self.open3ds_or_sxm)
        self.actionopenpythonbin.triggered.connect(self.openpythonbinfile)
        #self.actionopendidvdata.triggered.connect(self.opendidvdat)
        #self.actiondidvdatread.triggered.connect(self.didvdata)
        self.actionopenjavabin.triggered.connect(self.openjavabinfile)
        self.actionochooseimpurities.triggered.connect(self.choose_impurity)
        self.actionochooseBraggPeak.triggered.connect(self.choose_peak)
        self.actionoDoingDrfitCorrection.triggered.connect(self.driftcorrection)
        self.actioncutfigure.triggered.connect(self.cutfigure)
        self.actiondidvs.triggered.connect(self.didvmap)


        self.shortcut = QShortcut(QKeySequence('F3'),self.centralwidget,self.changecolor)
        self.shortcut_color_decrease = QShortcut(QKeySequence('F2'),self.centralwidget,self.changecolor_decrease)
        self.shortcut_1 = QShortcut(QKeySequence('Ctrl+Q'),self.centralwidget,self.dialog_open)
        self.shortcut_2 = QShortcut(QKeySequence('Ctrl+S'),self.centralwidget,self.savepng)
        self.shortcut_3 = QShortcut(QKeySequence('Ctrl+B'),self.centralwidget,self.savedata_bin)
        self.shortcut_4 = QShortcut(QKeySequence('F11'),self.centralwidget,self.contrast_ratio)
        self.shortcut_5 = QShortcut(QKeySequence('Ctrl+F'),self.centralwidget,self.fouriertransform)
        self.shortclipboard = QShortcut(QKeySequence('Ctrl+C'),self.centralwidget,self.to_clipboard)


        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def savepng(self):
        self.counts =self.counts +1
        self.ax.axis('off')
        self.figure.savefig(self.Newbinpath+'\\'+'topo'+'_'+str(self.counts)+'.eps',dpi=100,format='eps')
        self.figure.savefig(self.Newbinpath+'\\'+'topo'+'_'+str(self.counts)+'.png',dpi=600,format='png')
        self.ax.axis('on')
        self.topomap_draw(self.topo)

    def savedata_bin(self):
        self.count_bin = self.count_bin+1
        op.write_txt_without_series(self.Newbinpath,self.topo,'topo'+str(self.count_bin))
    def choosecolor(self):
        self.color = QColorDialog.getColor()


    def open3ds_or_sxm(self):
        self.filename, _ = QFileDialog.getOpenFileName(self.centralwidget, 'openfile', 'C:\\data')
        self.Newpath = op.openup(self.filename)
        # javabin.Nanoispy_Open(self.filename)


    def openjavabinfile(self):
        self.filename,_ =QFileDialog.getOpenFileName(self.centralwidget,'openfile','C:\\data','binfile(*.bin)')
        self.topo,self.Newbinpath = javabin.read_java_bin_single_layer(self.filename)
        self.topomap_draw(self.topo)


    def openpythonbinfile(self):
        self.filename, _ = QFileDialog.getOpenFileName(self.centralwidget,'openfile','C:\\data','binfile(*.bin)')
        self.topo, self.Newbinpath = wrb.read_bin(self.filename)
        self.topomap_draw(self.topo)

    def opendidvdata(self):
        self.filename,_ = QFileDialog.getOpenFileName(self.centralwidget,'opendata','C:\\data','datfile(*.dat')


    def choose_impurity(self):
        self.windows = Ui_Form_impurity(self.topo)
        self.windows.exec_()
        print("nihao")


    def choose_peak(self):
        self.fftdata = np.fft.fftshift(np.fft.fft2(self.topo))
        self.fftdata = np.log10(np.abs(self.fftdata) ** 2)
        self.ui = Ui_Form_bragg(self.fftdata)
        self.ui.exec_()

    def driftcorrection(self):
        self.Point_1_raw = []
        self.Point_2_raw = []
        for i in list(self.ui.datas.keys()):
            self.Point_1_raw.append(self.ui.datas[i][0])
            self.Point_2_raw.append(self.ui.datas[i][1])
        bragg_1,bragg_2 = fp.get_refine_bragg_point(self.fftdata,self.Point_1_raw,self.Point_2_raw)
        self.bragg_peak = np.empty((2,2))
        self.bragg_peak[0] = bragg_1
        self.bragg_peak[1] = bragg_2
        self.calc = UFiedlCalculation.UFieldCalculationReal(False,self.topo,60,self.bragg_peak,13,True)
        self.calc.doExpUCalc()
        self.calc.pickBestlayer()
        self.calc.makeBestUfield()
        self.calc.doRegularization()
        self.calc.addReglarization()
        self.calc.applyUfield()
        self.topomap_draw(self.topo)


    def cutfigure(self):
        self.windows = Ui_Form_Cut(self.topo)
        self.windows.exec_()
        new_topo = self.topo[int(self.windows.YPoint[1]):int(self.windows.YPoint[0]):1,int(self.windows.XPoint[0]):int(self.windows.XPoint[1]):1]
        print(np.shape(new_topo))
        print(self.windows.XPoint)
        print(self.windows.YPoint)
        self.topo = new_topo
        self.topomap_draw(self.topo)


    def didvmap(self):
        self.Windows = Ui_Form_didvmap(self.Newbinpath)
        self.Windows.show()

    def fouriertransform(self):
        if self.fft_count%2 ==0:
            self.fftdata = np.fft.fft2(self.topo)
            self.fftdata = np.log10(np.abs(np.fft.fftshift(self.fftdata))**2)
            self.topomap_draw(self.fftdata)
        elif self.fft_count%2 == 1:
            self.topomap_draw(self.topo)
        self.fft_count = self.fft_count + 1


    def fourier_draw(self,fftdata):
        self.ax.clear()
        self.ax.axis('on')
        self.ax.pcolormesh(fftdata,cmap=plt.get_cmap(self.cmap))
        self.canvas.draw()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "STM数据处理程序"))
        self.menu.setTitle(_translate("MainWindow", "打开文件"))
        self.menu_2.setTitle(_translate("MainWindow", "选择颜色"))
        self.menu_3.setTitle(_translate("MainWindow", "Phase Reference QPI"))
        self.menu_4.setTitle(_translate("MainWindow", "原子位置矫正"))
        self.menu_5.setTitle(_translate("MainWindow",'cut_picture'))
        self.menu_6.setTitle(_translate("MainWindow",'didv绘制'))
        self.actionchoose_color.setText(_translate("MainWindow", "颜色表"))
        self.actionopen3ds.setText(_translate("MainWindow", "open3ds"))
        self.actionopenpythonbin.setText(_translate("MainWindow", "openpythonbin"))
        self.actionopenjavabin.setText(_translate("MainWindow","openjavabin"))
        self.actionochooseimpurities.setText(_translate("MainWindow", "选取杂质"))
        self.actionoaddmask.setText(_translate("MainWindow", "addmask"))
        self.actionochooseBraggPeak.setText(_translate("MainWindow", "chooseBraggPeak"))
        self.actionoDoingDrfitCorrection.setText(_translate("MainWindow","DriftCorrection"))
        self.actioncutfigure.setText(_translate("MainWindow","cutfigure"))
        self.actiondidvs.setText(_translate("MainWindow",'didvmap'))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
