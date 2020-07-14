import os
import sys
import nanonispy as nap
import string
import numpy as np
import matplotlib.pyplot  as plt
import tkinter as tk
from tkinter import filedialog
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from scipy import interpolate
import struct
import itertools
from struct import unpack
from scipy.interpolate import interp1d
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline


# 打开 grid 文件
def openup(file_path):
    if os.path.splitext(file_path)[-1][1:] == '3ds':
        example = nap.read.Grid(file_path)
        _3ds_read(example, file_path)
    elif os.path.splitext(file_path)[-1][1:] == 'sxm':
        example1 = nap.read.Scan(file_path)
        _sxm_read(example1, file_path)


def read_bin(file_path):

    size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        header_size = struct.unpack('<i', f.read(4))
        shape = np.zeros(header_size[0] // 8, dtype='int')
        for i in range(header_size[0] // 8):
            s = struct.unpack('>d', f.read(8))
            shape[i] = s[0]
        # 此时shape是一个float数组
        print(shape)
        data_size = int((size - header_size[0] - 4) / 8)
        data_one_dimension = []
        for i in range(data_size):
            d = struct.unpack('>d', f.read(8))
            data_one_dimension.append(d[0])
        data = np.reshape(data_one_dimension, shape)
        dirname, basename = os.path.split(file_path)
    return data, dirname


def _3ds_read(example, file_path):
    paths, files = os.path.split(file_path)
    name = os.path.splitext(files)[0]
    rs = os.path.splitext(files)[-1][1:]
    New_path = paths + '/rawdata' + '_' + name + '_' + rs
    # lists = list(example.signals.keys())
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    for i in example.signals.keys():
        if i == 'params':
            pass
        else:
            result = i.rfind('/') != -1
            if result:
                i_new = i.replace('/', '_')
            else:
                i_new = i
            file = open(New_path + '/' + i_new + '.bin', 'wb')
            # 这里我们需要定义binary file 的头文件
            data = example.signals.get(i)  # 这里得到的数据是元组数据
            datas = np.asarray(data, dtype='>d', order='C')
            shapes = datas.shape
            size = len(shapes) * struct.calcsize('>d')
            file.write(struct.pack('<i', size))
            for i in shapes:
                file.write(struct.pack('>d', i))
            data_one_dimension = datas.flatten()
            for i in range(len(data_one_dimension)):
                file.write(struct.pack('>d', data_one_dimension[i]))
    return New_path


def _sxm_read(example, file_path):
    paths, files = os.path.split(file_path)
    name = os.path.splitext(files)[0]
    rs = os.path.splitext(files)[-1][1:]
    New_path = paths + '/rawdata' + '_' + name + '_' + rs
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    for i in example.signals.keys():
        if i == 'params':
            pass
        else:
            result = i.rfind('/') != -1
            if result:
                i_new = i.replace('/', '_')
            else:
                i_new = i
            data = example.signals.get(i)
            if isinstance(data, dict):
                for keys in data.keys():
                    file = open(New_path + '/' + i_new + '_' + keys + '.bin', 'wb')
                    datas = np.asarray(data[keys], dtype='>d', order='C')
                    shapes = datas.shape
                    size = len(shapes) * struct.calcsize('>d')
                    file.write(struct.pack('<i', size))
                    for i in shapes:
                        file.write(struct.pack('>d', i))
                    data_one_dimension = datas.flatten()
                    for i in range(len(data_one_dimension)):
                        file.write(struct.pack('>d', data_one_dimension[i]))
            else:
                file = open(New_path, '/' + i_new + '.bin', 'wb')
                datas = np.asarray(data[keys], dtype='>d', order='C')
                shapes = datas.shape
                size = len(shapes) * struct.calcsize('>d')
                file.write(struct.pack('<i', size))
                for i in shapes:
                    file.write(struct.pack('>d', i))
                    data_one_dimension = datas.flatten()
                for i in range(len(data_one_dimension)):
                    file.write(struct.pack('>d', data_one_dimension[i]))
    return New_path