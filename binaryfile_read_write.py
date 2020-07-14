import os
import sys
import string
import tkinter as tk
from tkinter import filedialog
import struct
from struct import unpack
import numpy as np
import inspect, re

def varname(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)

def write_bin_single(filepath,ans,name1):
    New_path = filepath +'/'+'Ufield'
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    datas = ans.astype('>d')
    shapes = datas.shape
    size = len(shapes)*struct.calcsize('>d')
    file = open(New_path+'/'+name1+'.bin','wb')
    file.write(struct.pack('<i',size))
    for i in shapes:
        file.write(struct.pack('>d',i))
    data_one_dimension = datas.flatten()
    for i in range(len(data_one_dimension)):
        file.write(struct.pack('>d',data_one_dimension[i]))

def write_bin(filepath,ux,uy):
    New_path =  filepath +'/'+'Ufield'
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    name1 = varname(ux)
    datas = ux.astype('>d')
    shapes = datas.shape
    size = len(shapes)*struct.calcsize('>d')
    file = open(New_path+'/'+name1+'.bin','wb')
    file.write(struct.pack('<i',size))
    for i in shapes:
        file.write(struct.pack('>d',i))
    data_one_dimension = datas.flatten()
    for i in range(len(data_one_dimension)):
        file.write(struct.pack('>d',data_one_dimension[i]))
    name2 = varname(uy)
    datay = ux.astype('>d')
    shapes = datay.shape
    size = len(shapes)*struct.calcsize('>d')
    file = open(New_path+'/'+name2+'.bin','wb')
    file.write(struct.pack('<i',size))
    for i in shapes:
        file.write(struct.pack('>d',i))
    data_one_dimension = datay.flatten()
    for i in range(len(data_one_dimension)):
        file.write(struct.pack('>d',data_one_dimension[i]))
def read_bin(file_path):
    size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        header_size = struct.unpack('<i', f.read(4))
        shape = np.zeros(header_size[0] // 8, dtype='int')
        for i in range(header_size[0] // 8):
            s = struct.unpack('>d', f.read(8))
            shape[i] = s[0]
        print(shape)
        data_size = int((size - header_size[0] - 4) / 8)
        data_one_dimension = []
        for i in range(data_size):
            d = struct.unpack('>d', f.read(8))
            data_one_dimension.append(d[0])
        data = np.reshape(data_one_dimension, shape)
        dirname, basename = os.path.split(file_path)
    return data, dirname

def write_bin_with_name(filepath,ans,name):
    New_path = filepath +'/'+'Ufield'
    if not os.path.exists(New_path):
        os.makedirs(New_path)
    datas = ans.astype('>d')
    shapes = datas.shape
    size = len(shapes)*struct.calcsize('>d')
    file = open(New_path+'/'+name+'.bin','wb')
    file.write(struct.pack('<i',size))
    for i in shapes:
        file.write(struct.pack('>d',i))
    data_one_dimension = datas.flatten()
    for i in range(len(data_one_dimension)):
        file.write(struct.pack('>d',data_one_dimension[i]))