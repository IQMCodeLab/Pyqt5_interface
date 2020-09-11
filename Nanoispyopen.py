import os
import nanonispy as nap
import numpy as np
import struct
def openup(file_path):
    if os.path.splitext(file_path)[-1][1:] == '3ds':
        example = nap.read.Grid(file_path)
        _3ds_read(example, file_path)
    elif os.path.splitext(file_path)[-1][1:] == 'sxm':
        example1 = nap.read.Scan(file_path)
        _sxm_read(example1, file_path)


def _3ds_read(example, file_path):
    paths, files = os.path.split(file_path)
    name = os.path.splitext(files)[0]
    rs = os.path.splitext(files)[-1][1:]
    New_path = paths + '/rawdata' + '_' + name + '_' + rs
    # lists = list(example.signals.keys())

    if not os.path.exists(New_path):
        os.makedirs(New_path)
    position_xy = example.header.get('pos_xy')
    dim = example.header.get('dim_px')
    nx = dim[0]
    ny = dim[1]
    size_xy = example.header.get('size_xy')
    point_x = position_xy[0]
    point_y = position_xy[1]
    lx = size_xy[0]
    ly = size_xy[1]
    x = np.linspace(point_x-lx/2,point_x+lx/2,nx)
    y = np.linspace(point_x-ly/2,point_y+ly/2,ny)
    sweep_signal = example.signals.get('sweep_signal')

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
            shapes = data.shape
            if len(shapes) == 3:
                write_three_dimensional_bin(file,data,sweep_signal,x,y)
            if len(shapes) == 2:
                write_two_dimensional_bin(file,data,x,y)
            if len(shapes) == 1:
                write_one_dimensional_bin(file,data)
    return New_path


def _sxm_read(example, file_path):
    paths, files = os.path.split(file_path)
    name = os.path.splitext(files)[0]
    rs = os.path.splitext(files)[-1][1:]
    New_path = paths + '/rawdata' + '_' + name + '_' + rs
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    position_xy = example.header.get('scan_offset')
    dim = example.header.get('scan_pixels')
    nx = dim[0]
    ny = dim[1]
    size_xy = example.header.get('scan_range')
    point_x = position_xy[0]
    point_y = position_xy[1]
    lx = size_xy[0]
    ly = size_xy[1]
    x = np.linspace(point_x - lx / 2, point_x + lx / 2, nx)
    y = np.linspace(point_x - ly / 2, point_y + ly / 2, ny)
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
                    datas = data[keys]
                    write_two_dimensional_bin(file,datas,x,y)
            else:
                file = open(New_path, '/' + i_new + '.bin', 'wb')
                datas = data[keys]
                write_two_dimensional_bin(file,datas,x,y)
    return New_path


def write_three_dimensional_bin(file,data,sweep_signals,x,y):
    len_x,len_y,len_z = np.shape(data)
    datas = struct.pack('>i',len_x)
    file.write(datas)
    datas = struct.pack('>i',len_y)
    file.write(datas)
    datas = struct.pack('>i',len_z)
    file.write(datas)
    z = sweep_signals
    for i in range(len_x):
        datas =struct.pack('>d',x[i])
        file.write(datas)
    for i in range(len_y):
        datas = struct.pack('>d',y[i])
        file.write(datas)
    for i in range(len_z):
        datas = struct.pack('>d',z[i])
        file.write(datas)
    for n in range(len_z):
        for i in range(len_x):
            for j in range(len_y):
                datas = struct.pack('>d',data[j][i][n])
                file.write(datas)


def write_two_dimensional_bin(file,data,x,y):
    len_x,len_y = np.shape(data)
    datas = struct.pack('>i',len_x)
    file.write(datas)
    datas = struct.pack('>i',len_y)
    file.write(datas)
    datas=struct.pack(">d",1.0)
    file.write(datas)
    datas=struct.pack(">d",1.0)
    file.write(datas)
    for i in range(len_x):
        datas = struct.pack('>d', x[i])
        file.write(datas)
    for i in range(len_y):
        datas = struct.pack('>d', y[i])
        file.write(datas)
    for i in range(len_x):
        for j in range(len_y):
            datas = struct.pack('>d', data[j][i])
            file.write(datas)
    file.close()


def write_one_dimensional_bin(file,data):
    len_x = len(data)
    datas = struct.pack('>i',len_x)
    file.write(datas)
    for i in range(len_x):
        datas = struct.pack('>d',data[i])
        file.write(datas)
    file.close()

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
openup(file_path)

