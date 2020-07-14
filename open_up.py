import sys
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
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline


def openup():
    root = tk.Tk()
    root.withdraw()
    global len_x
    global len_y
    file_path = filedialog.askopenfilename()
    example = nap.read.Grid(file_path)
    # 上面两行是用来读取所要读取的data数据的

    lockin = example.signals.get("Current (A)")
    # lockinb = example.signals.get("LI Demod 1 Y (A)")
    bias_volt = example.signals.get("sweep_signal")
    z_data = example.signals.get('topo')
    # 这里依旧需要去学会使用
    len_x = np.shape(lockin)[0]
    len_y = np.shape(lockin)[1]
    # 数据的维度读取
    return len_x, len_y, bias_volt, lockin, z_data


openups = openup()


# smooth函数；插值函数的调用也是问题，
def smooth(len_x, len_y, bias_volt, lockin):
    Precision = 1000
    bias_volt_new = np.zeros((Precision))
    lockin_smooth = np.zeros((len_x, len_y, Precision))
    bias_volt_new = np.linspace(max(bias_volt), min(bias_volt), Precision)
    for i in range(len_x):
        for j in range(len_y):
            lockin_xy = lockin[i, j, :]
            tck = interpolate.splrep(bias_volt, lockin_xy)
            lockin_smooth[i, j, :] = interpolate.splev(bias_volt_new, tck)
    return bias_volt_new, lockin_smooth


smooths = smooth(openups[0], openups[1], openups[2], openups[3])


def find_min(bias_volt_new, lockin_smooth):
    min_position = np.unravel_index(np.argmin(lockin_smooth), lockin_smooth.shape)
    print("最小值是{},此时的偏压为{},位于第x={},y={}个点".format(lockin_smooth[min_position], bias_volt_new[min_position[2]],
                                                  min_position[0], min_position[1]))
    return min_position


find_min(smooths[0], smooths[1])
