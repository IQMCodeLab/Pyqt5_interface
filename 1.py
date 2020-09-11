# coding=utf8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
多窗口交互---直接访问对应的控件，代码的耦合度高
方式1 直接访问控件
"""

# from DataDialog import DateDialog
#
# class MultiWindow1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(" 多窗口交互")
#
#         self.lineEdit = QLineEdit(self)
#         self.button1 = QPushButton('弹出对话框1')
#         self.button1.clicked.connect(self.onButton1Click)
#
#         self.button2 = QPushButton('弹出对话框2')
#         self.button2.clicked.connect(self.onButton2Click)
#
#         gridLayout = QGridLayout()
#         gridLayout.addWidget(self.button1)
#         gridLayout.addWidget(self.button2)
#         gridLayout.addWidget(self.lineEdit)
#
#         self.setLayout(gridLayout)
#
#     def onButton1Click(self):
#         dialog = DateDialog(self)
#         # 对话框保持悬浮
#         result = dialog.exec()
#         date = dialog.dateTime()
#         self.lineEdit.setText(date.date().toString())
#         dialog.destroy()
#
#     def onButton2Click(self):
#         date,time,result = DateDialog.getDateTime()
#         self.lineEdit.setText(date.toString())
#         if result == QDialog.Accepted:
#             print("点击确定按钮")
#         else:
#             print('单击取消按钮')
# coding=utf8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
多窗口交互---直接访问对应的控件，代码的耦合度高
方式1 直接访问控件
"""

# from DataDialog import DateDialog
#
# class MultiWindow1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(" 多窗口交互")
#
#         self.lineEdit = QLineEdit(self)
#         self.button1 = QPushButton('弹出对话框1')
#         self.button1.clicked.connect(self.onButton1Click)
#
#         self.button2 = QPushButton('弹出对话框2')
#         self.button2.clicked.connect(self.onButton2Click)
#
#         gridLayout = QGridLayout()
#         gridLayout.addWidget(self.button1)
#         gridLayout.addWidget(self.button2)
#         gridLayout.addWidget(self.lineEdit)
#
#         self.setLayout(gridLayout)
#
#     def onButton1Click(self):
#         dialog = DateDialog(self)
#         # 对话框保持悬浮
#         result = dialog.exec()
#         date = dialog.dateTime()
#         self.lineEdit.setText(date.date().toString())
#         dialog.destroy()
#
#     def onButton2Click(self):
#         date,time,result = DateDialog.getDateTime()
#         self.lineEdit.setText(date.toString())
#         if result == QDialog.Accepted:
#             print("点击确定按钮")
#         else:
#             print('单击取消按钮')
"""
多窗口交互，使用信号与槽函数
这样就可以降低代码的耦合度： 信号：创建、触发、连接
"""
#coding=utf8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
"""
多窗口交互---直接访问对应的控件，代码的耦合度高
方式1 直接访问控件
"""

# from DataDialog import DateDialog
#
# class MultiWindow1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(" 多窗口交互")
#
#         self.lineEdit = QLineEdit(self)
#         self.button1 = QPushButton('弹出对话框1')
#         self.button1.clicked.connect(self.onButton1Click)
#
#         self.button2 = QPushButton('弹出对话框2')
#         self.button2.clicked.connect(self.onButton2Click)
#
#         gridLayout = QGridLayout()
#         gridLayout.addWidget(self.button1)
#         gridLayout.addWidget(self.button2)
#         gridLayout.addWidget(self.lineEdit)
#
#         self.setLayout(gridLayout)
#
#     def onButton1Click(self):
#         dialog = DateDialog(self)
#         # 对话框保持悬浮
#         result = dialog.exec()
#         date = dialog.dateTime()
#         self.lineEdit.setText(date.date().toString())
#         dialog.destroy()
#
#     def onButton2Click(self):
#         date,time,result = DateDialog.getDateTime()
#         self.lineEdit.setText(date.toString())
#         if result == QDialog.Accepted:
#             print("点击确定按钮")
#         else:
#             print('单击取消按钮')
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 331)
        self.runButton = QtWidgets.QPushButton(Form)
        self.runButton.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.runButton.setObjectName("runButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 431, 192))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qthread Example"))
        self.runButton.setText(_translate("Form", "Run"))
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyMainForm(QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 实例化线程对象
        self.work = WorkThread()
        self.runButton.clicked.connect(self.execute)

    def execute(self):
        # 启动线程
        self.work.start()
        # 线程自定义信号连接的槽函数
        self.work.trigger.connect(self.display)

    def display(self,str):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        self.listWidget.addItem(str)

class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        #重写线程执行的run函数
        #触发自定义信号
        for i in range(20):
            time.sleep(1)
            # 通过自定义信号把待显示的字符串传递给槽函数
            self.trigger.emit(str(i))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(327, 303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.open_dialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "多线程弹窗"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 128)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
class DialogWindow(QDialog, Ui_Dialog):
    stop_thread = pyqtSignal()  # 定义关闭子线程的信号

    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)

    def update_progressbar(self, p_int):
        self.progressBar.setValue(p_int)

    def closeEvent(self, event):
        self.stop_thread.emit()
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = 0

    def open_dialog(self):
        dialog = DialogWindow(self)
        dialog.show()
        self.thread = RunThread(self.count)
        self.count += 1
        self.thread.update_pb.connect(dialog.update_progressbar)
        dialog.stop_thread.connect(self.thread.terminate)
        self.thread.start()

import time 
class RunThread(QThread):
    update_pb = pyqtSignal(int)

    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        for i in range(1, 101):
            print('thread_%s' % self.count, i, QThread().currentThreadId())
            self.update_pb.emit(i)
            time.sleep(1)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time


# 继承QThread
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            time.sleep(0.2)
            self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同


class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # 按钮初始化
        self.button = QtWidgets.QPushButton('开始', self)
        self.button.setToolTip('这是一个 <b>QPushButton</b> widget')
        self.button.resize(self.button.sizeHint())
        self.button.move(120, 80)
        self.button.clicked.connect(self.start_login)  # 绑定多线程触发事件

        # 进度条设置
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(50, 50, 210, 25)
        self.pbar.setValue(0)

        # 窗口初始化
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('OmegaXYZ.com')
        self.show()

        self.thread = None  # 初始化线程

    def start_login(self):
        # 创建线程
        self.thread = Runthread()
        # 连接信号
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def call_backlog(self, msg):
        self.pbar.setValue(int(msg))  # 将线程的参数传入进度条


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Example()
    myshow.show()
    sys.exit(app.exec_())

# 主窗口
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.pushButton.setText(_translate("MainWindow", "打开窗口1"))
        self.pushButton_2.setText(_translate("MainWindow", "打开窗口2 "))


# 窗口1
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 100, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "这是窗口1"))


# 窗口2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 140, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "这是窗口2"))


# 主程序
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.window2 = Ui_Dialog()
        self.window2.setupUi()
        self.window3 = Ui_Form()
        self.window3.setupUi()
        self.pushButton.clicked.connect(self.window2.show)  # 绑定窗口2
        self.pushButton_2.clicked.connect(self.window3.show)  # 绑定窗口3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class InputdialogDemo(QWidget):
    def __init__(self, parent=None):

        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()

        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获取字符串")
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获取整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog例子")

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select Input dialog", "编程语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog \n nihao', '输入姓名\n nihao')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", '请输入数字')
        if ok:
            self.le3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InputdialogDemo()
    win.show()
    sys.exit(app.exec_())

import pickle
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')
import matplotlib.patches as patches
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class SurfViewer(QMainWindow):
    def __init__(self, parent=None):
        super(SurfViewer, self).__init__()
        self.parent = parent
        self.centralWidget = QWidget()
        self.color = self.centralWidget.palette().color(QPalette.Background)
        self.setCentralWidget(self.centralWidget)
        self.plotview = QGroupBox(" ")
        self.layout_plotview = QVBoxLayout()
        self.mascenelfp = lfpViewer(self)
        self.layout_plotview.addWidget(self.mascenelfp)
        self.centralWidget.setLayout(self.layout_plotview)


class lfpViewer(QGraphicsView):
    def __init__(self, parent=None):
        super(lfpViewer, self).__init__(parent)
        self.parent=parent
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setBackgroundBrush(QBrush(self.parent.color))# self.setBackgroundBrush(QBrush(QColor(200, 200, 200)))
        self.figure = plt.figure(facecolor=[self.parent.color.red()/255,self.parent.color.green()/255,self.parent.color.blue()/255]) #Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.save_button = QPushButton()
        self.save_button.setIcon(QIcon(os.path.join('icons','SaveData.png')))
        self.save_button.setToolTip("Save Figure Data")
        self.toolbar.addWidget(self.save_button)
        self.save_button.clicked.connect(self.saveFigData)
        self.load_button = QPushButton()
        self.load_button.setIcon(QIcon(os.path.join('icons','LoadData.png')))
        self.load_button.setToolTip("Load Figure Data")
        self.toolbar.addWidget(self.load_button)
        self.load_button.clicked.connect(self.loaddatapickle)
        if 0:
            t=np.arange(1000)
            self.axes_l=self.figure.add_subplot(311)
            self.axes_l.plot(t, np.sin(2*3.14*100*t))
            self.axes_Y=self.figure.add_subplot(312)
            self.axes_Y.plot(t, np.cos(2*3.14*100*t))
            self.axes_Yi=self.figure.add_subplot(313)
            self.axes_Yi.plot(t, np.tan(2*3.14*100*t))


        self.canvas.setGeometry(0, 0, 1600, 500 )
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def loaddatapickle(self):
        fileName = QFileDialog.getOpenFileName(self,'Load Data', '', 'pickle (*.pickle)')
        if  (fileName[0] == '') :
            return
        fileName = str(fileName[0])
        filehandler = open(fileName , 'rb')
        self.figure = pickle.load(filehandler)
        filehandler.close()
        self.canvas.draw()
        self.parent.parent.processEvents()
        return

    def saveFigData(self):
        fileName = QFileDialog.getSaveFileName(self,'Save Figure Data', '', 'pickle (*.pickle)')
        if  (fileName[0] == '') :
            return
        fileName = str(fileName[0])
        file_pi = open(fileName, 'wb')
        pickle.dump(self.figure, file_pi, -1)
        file_pi.close()
        return


def main():
    app = QApplication(sys.argv)
    ex = SurfViewer(app)
    ex.showMaximized()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 200, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 141, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "这是Line Edit ->"))
        self.label_2.setText(_translate("Dialog", "这是Text Browser ->"))


class Dialog(QtWidgets.QDialog):
    对QDialog类重写，实现一些功能

    def closeEvent(self, event):
        
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    #主函数，用于运行程序
    #:return: None

    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()  # 注意修改为了自己重写的Dialog类
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()  # 显示了自己重写的Dialog类
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

#窗口之间数据传递（通过属性来进行消息传递）
from PyQt5.QtWidgets import QDialogButtonBox, QDateTimeEdit,QDialog,QComboBox,QTableView,QAbstractItemView,QHeaderView,QTableWidget, QTableWidgetItem, QMessageBox,QListWidget,QListWidgetItem, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel,QCursor,QFont,QBrush,QColor,QPainter,QMouseEvent,QImage,QTransform
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize,Qt,QObject,pyqtSignal,QTimer,QEvent,QDateTime,QDate

import sys
class Win(QWidget):
    def __init__(self,parent=None):
        super(Win, self).__init__(parent)
        self.resize(400,400)

        self.btn=QPushButton("按钮",self)
        self.btn.move(50,50)
        self.btn.setMinimumWidth(80)

        #显示子窗口传来的日期字符串或者其他数据
        self.label=QLabel('显示信息',self)
        self.label.setMinimumWidth(420)

        self.btn.clicked.connect(self.fn)
    def fn(self):
        date,time,res= Dialog.getResult(self)
        print(date,time,res)
        #或者下面写法，上面使用了下面定义的静态方法，下面则直接实例化自定义的对话框类
        # dialog=Dialog()
        # res=dialog.exec_()
        # date=dialog.datetime.date()
        # time=dialog.datetime.time()
        # print(res,date,time)

#弹出框对象
class Dialog(QDialog):

    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        layout=QVBoxLayout(self)
        self.label=QLabel(self)
        self.datetime=QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        self.label.setText("请选择日期")
        layout.addWidget(self.label)
        layout.addWidget(self.datetime)

        buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)#点击ok，隐士存在该方法
        buttons.rejected.connect(self.reject)#点击cancel，该方法默认隐士存在
        layout.addWidget(buttons)
            #该方法在父类方法中调用，直接打开了子窗体，返回值则用于向父窗体数据的传递
    @staticmethod
    def getResult(self,parent=None):
        dialog=Dialog(parent)
        result=dialog.exec_()
        d=dialog.datetime.dateTime()
        return (d.date(),d.time(),result)

if __name__=='__main__':

    app=QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


MAXVAL = 650000

class RangeSliderClass(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.minTime = 0
        self.maxTime = 0
        self.minRangeTime = 0
        self.maxRangeTime = 0

        self.sliderMin = -50
        self.sliderMax = 50

        self.setupUi(self)

    def setupUi(self, RangeSlider):
        RangeSlider.setObjectName("RangeSlider")
        RangeSlider.resize(1000, 65)
        RangeSlider.setMaximumSize(QtCore.QSize(16777215, 65))
        self.RangeBarVLayout = QtWidgets.QVBoxLayout(RangeSlider)
        self.RangeBarVLayout.setContentsMargins(5, 0, 5, 0)
        self.RangeBarVLayout.setSpacing(0)
        self.RangeBarVLayout.setObjectName("RangeBarVLayout")

        self.slidersFrame = QtWidgets.QFrame(RangeSlider)
        self.slidersFrame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.slidersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slidersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slidersFrame.setObjectName("slidersFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.slidersFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(10, 2, 10, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ## Start Slider Widget
        self.startSlider = QtWidgets.QSlider(self.slidersFrame)
        self.startSlider.setMaximum(50)
        self.startSlider.setMinimum(0)
        self.startSlider.setMinimumSize(QtCore.QSize(100, 5))
        self.startSlider.setMaximumSize(QtCore.QSize(16777215, 10))

        font = QtGui.QFont()
        font.setKerning(True)

        self.startSlider.setFont(font)
        self.startSlider.setAcceptDrops(False)
        self.startSlider.setAutoFillBackground(False)
        self.startSlider.setOrientation(QtCore.Qt.Horizontal)
        self.startSlider.setInvertedAppearance(True)
        self.startSlider.setObjectName("startSlider")
        self.startSlider.setValue(0)
        self.startSlider.valueChanged.connect(self.handleStartSliderValueChange)
        self.horizontalLayout.addWidget(self.startSlider)

        ## End Slider Widget
        self.endSlider = QtWidgets.QSlider(self.slidersFrame)
        self.endSlider.setMaximum(0)
        self.endSlider.setMinimum(-50)
        self.endSlider.setMinimumSize(QtCore.QSize(100, 5))
        self.endSlider.setMaximumSize(QtCore.QSize(16777215, 10))
        self.endSlider.setTracking(True)
        self.endSlider.setOrientation(QtCore.Qt.Horizontal)
        self.endSlider.setObjectName("endSlider")
        self.endSlider.setValue(0)
        self.endSlider.valueChanged.connect(self.handleEndSliderValueChange)

        #self.endSlider.sliderReleased.connect(self.handleEndSliderValueChange)

        self.horizontalLayout.addWidget(self.endSlider)

        self.RangeBarVLayout.addWidget(self.slidersFrame)

        #self.retranslateUi(RangeSlider)
        QtCore.QMetaObject.connectSlotsByName(RangeSlider)

        self.show()

    @QtCore.pyqtSlot(int)
    def handleStartSliderValueChange(self, value):
        self.startSlider.setValue(value)
        print(value)
        print(1)

    @QtCore.pyqtSlot(int)
    def handleEndSliderValueChange(self, value):
        self.endSlider.setValue(value)
        print(value)




app = QtWidgets.QApplication(sys.argv)
awindow = RangeSliderClass()
sys.exit(app.exec_())

# slide Bar Range example.
# max min interval + date example.
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
MAXVAL = 650000
class RangeSliderClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.minTime = 0
        self.maxTime = 0
        self.minRangeTime = 0
        self.maxRangeTime = 0
        self.sliderMin = MAXVAL
        self.sliderMax = MAXVAL
        self.setupUi(self)
    def setupUi(self, RangeSlider):
        RangeSlider.setObjectName("RangeSlider")
        RangeSlider.resize(1000, 65)
        RangeSlider.setMaximumSize(QtCore.QSize(16777215, 65))
        self.RangeBarVLayout = QtWidgets.QVBoxLayout(RangeSlider)
        self.RangeBarVLayout.setContentsMargins(5, 0, 5, 0)
        self.RangeBarVLayout.setSpacing(0)
        self.RangeBarVLayout.setObjectName("RangeBarVLayout")
        self.slidersFrame = QtWidgets.QFrame(RangeSlider)
        self.slidersFrame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.slidersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slidersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slidersFrame.setObjectName("slidersFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.slidersFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        ## Start Slider Widget
        self.startSlider = QtWidgets.QSlider(self.slidersFrame)
        self.startSlider.setMaximum(self.sliderMin)
        self.startSlider.setMinimumSize(QtCore.QSize(100, 5))
        self.startSlider.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setKerning(True)
        self.startSlider.setFont(font)
        self.startSlider.setAcceptDrops(False)
        self.startSlider.setAutoFillBackground(False)
        self.startSlider.setOrientation(QtCore.Qt.Horizontal)
        self.startSlider.setInvertedAppearance(True)
        self.startSlider.setObjectName("startSlider")
        self.startSlider.setValue(MAXVAL)
        self.startSlider.valueChanged.connect(self.handleStartSliderValueChange)
        self.horizontalLayout.addWidget(self.startSlider)
        ## End Slider Widget
        self.endSlider = QtWidgets.QSlider(self.slidersFrame)
        self.endSlider.setMaximum(MAXVAL)
        self.endSlider.setMinimumSize(QtCore.QSize(100, 5))
        self.endSlider.setMaximumSize(QtCore.QSize(16777215, 10))
        self.endSlider.setTracking(True)
        self.endSlider.setOrientation(QtCore.Qt.Horizontal)
        self.endSlider.setObjectName("endSlider")
        self.endSlider.setValue(self.sliderMax)
        self.endSlider.valueChanged.connect(self.handleEndSliderValueChange)
        #self.endSlider.sliderReleased.connect(self.handleEndSliderValueChange)
        self.horizontalLayout.addWidget(self.endSlider)
        self.RangeBarVLayout.addWidget(self.slidersFrame)
        #self.retranslateUi(RangeSlider)
        QtCore.QMetaObject.connectSlotsByName(RangeSlider)
        self.show()
    @QtCore.pyqtSlot(int)
    def handleStartSliderValueChange(self, value):
        self.startSlider.setValue(value)
    @QtCore.pyqtSlot(int)
    def handleEndSliderValueChange(self, value):
        self.endSlider.setValue(value)
app = QtWidgets.QApplication(sys.argv)
awindow = RangeSliderClass()
sys.exit(app.exec_())
"""
import nanonispy
import  matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter,AutoMinorLocator
x1 =[0,5000,10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000];
y1=[0, 223, 488, 673, 870, 1027, 1193, 1407, 1609, 1791, 2113, 2388];

x2 =[0,5000,10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000];
y2=[0, 214, 445, 627, 800, 956, 1090, 1281, 1489, 1625, 1896, 2151];

fig,ax = plt.subplots(figsize=(12,10))
font1 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 30,
}
majorLocator_x = MultipleLocator(12000)
#majorFormatter = FormatStrFormatter('%d')
minorLocator_x = MultipleLocator(6000)
majorLocator_y = MultipleLocator(600)
minorLocator_y = MultipleLocator(300)
A,=ax.plot(x1,y1,'-r',label='A',linewidth =2)
B,=ax.plot(x2,y2, '-b',label= 'B',linewidth=2)
ax.tick_params(which='minor',direction='in',length =6,width=2,labelsize=22,axis='both')
ax.tick_params(which='major',direction='in',length =12,width =2,labelsize=22)
#labels = ax.get_xticklabels() + ax.get_yticklabels()
#[label.set_fontname('Arial') for label in labels]
ax.xaxis.set_major_locator(majorLocator_x)
#ax.xaxis.set_major_formatter(majorFormatter)
ax.xaxis.set_minor_locator(minorLocator_x)
#ax.xaxis.set_minor_formatter(majorFormatter)
ax.yaxis.set_major_locator(majorLocator_y)
#ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator_y)
#ax.yaxis.set_minor_formatter(majorFormatter)
ax2 = fig.gca()
bwitch = 2
ax2.spines['top'].set_linewidth(bwitch)
ax2.spines['left'].set_linewidth(bwitch)
ax2.spines['right'].set_linewidth(bwitch)
ax2.spines['bottom'].set_linewidth(bwitch)
plt.xticks(fontproperties = 'Arial',size=22)
plt.yticks(fontproperties = 'Arial',size=22)
#ax.set_yticks(fontproperties = 'Arial',size=30)
#ax.ylim(0,3000)
lengend = ax.legend(loc ='upper right',fancybox = True,handles=[A,B],prop=font1)
ax.set_xlabel('Bias (V)',font1)
ax.set_ylabel('dI/dV (a.u)',font1)
ax.set_xlim(-1000,62000)
#plt.ylim(-100,2500)
#plt.xlim(-1000,62000)

plt.show()

