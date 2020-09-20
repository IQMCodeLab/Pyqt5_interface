import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def subtractlineavg(data,X_Y):
    mean = 0
    len_y,len_x = np.shape(data)
    if X_Y:
        for i in range(len_y):
            mean = np.mean(data[i,:])
            for j in range(len_x):
                data[i][j] = data[i][j]-mean
    else:
        for x in range(len_x):
            mean = np.mean(data[:,x])
            for y in range(len_y):
                data[y,x] = data[y][x] - mean
    return data


"""
我们使用的回归模型是 sklearn里面的，著名的线性回归模型
"""
def subtractLinefit(data,horizontal):
    mean = 0
    len_y,len_x = np.shape(data)
    x = np.empty(len_x)
    y = np.empty(len_y)
    index_x = np.linspace(0,len_x,len_x)
    index_y = np.linspace(0,len_y,len_y)
    index_x = index_x[:,np.newaxis]
    index_y = index_y[:,np.newaxis]
    if horizontal:
        for i in range(len_y):
            x = data[i,:]
            #x = x[:,np.newaxis]
            model = LinearRegression()
            model.fit(index_x,x)
            predicts = model.predict(index_x)
            data[i,:] =data[i,:] - predicts
    else:
        for i in range(len_x):
            y = data[:,i]
            #y = y[:,np.newaxis]
            model = LinearRegression()
            model.fit(index_y,y)
            predicts = model.predict(index_y)
            data[:,i] = data[:,i]-predicts
    return data


def subtract_avg(data):
    mean_data = np.mean(data)
    data = data - mean_data
    return data


import fieldops
from PyQt5.QtWidgets import QDialog,QInputDialog
def dialog_function(centerwidget,topo):
    items = ('raw', 'subtract best-fit line from horizontal lines',
             'subtract best-fit line form vertical lines',
             'subtract average from horizontal lines',
             'subtract average from vertical lines',
             'Nomalize to the range [0,1]',
             'suppress bad pixels',
             'subtract average for all data'
             'subtract linear fit',
             'subtract plane fit')
    item, ok = QInputDialog.getItem(centerwidget, 'scan correction', 'fit list', items, 0, False)
    if ok and item:
        if item == 'raw':
            topo = topo
            print("形貌图保持不变")
        elif item == 'subtract plane fit':
            topo = fieldops.subtractMeanPlane(topo)
            print("形貌图planefit")
        elif item == 'suppress bad pixels':
            topo = fieldops.detectNaN(topo)
        elif item == 'subtract best-fit line form vertical lines':
            topo = subtractLinefit(topo,False)
        elif item == 'subtract best-fit line form horizontal lines':
            topo = subtractLinefit(topo,True)
        elif item == 'subtract average from vertical lines':
            topo = subtractlineavg(topo,False)
        elif item == 'subtract average for all data':
            topo=subtract_avg(topo)
        elif item == 'subtract average from horizontal lines':
            topo = subtractlineavg(topo,True)

    return topo