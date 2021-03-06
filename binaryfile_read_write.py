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
import numpy as np
import matplotlib.pyplot as plt
import struct
def read_java_bin_multi(filepath):
    file = open(filepath,'rb')
    nx = int(struct.unpack(">i",file.read(4))[0])
    ny = int(struct.unpack(">i",file.read(4))[0])
    nlayers = int(struct.unpack(">i", file.read(4))[0])
    x=np.zeros(nx,dtype=np.float64)
    y=np.zeros(ny,dtype=np.float64)
    v=np.zeros(nlayers,dtype=np.float64)
    for i in range(nx):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        x[i] = data
    for j in range(ny):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        # y[j]=data
    for n in range(nlayers):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        v[n] = data
    dataset = np.zeros((nlayers, nx, ny), dtype=np.float64)
    for n in range(nlayers):
        for i in range(nx):
            for j in range(ny):
                data = np.float64(struct.unpack(">d", file.read(8))[0])
                dataset[n][i][j] = data
def transform_multi_layer_single_layer(filepath):
    file = open(filepath,'rb')
    nx = int(struct.unpack(">i",file.read(4))[0])
    ny = int(struct.unpack(">i",file.read(4))[0])
    nlayers = int(struct.unpack(">i", file.read(4))[0])
    x=np.zeros(nx,dtype=np.float64)
    y=np.zeros(ny,dtype=np.float64)
    v=np.zeros(nlayers,dtype=np.float64)
    for i in range(nx):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        x[i] = data
    for j in range(ny):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        # y[j]=data
    for n in range(nlayers):
        data = np.float64(struct.unpack(">d", file.read(8))[0])
        v[n] = data
    dataset = np.zeros((nlayers, nx, ny), dtype=np.float64)
    for n in range(nlayers):
        for i in range(nx):
            for j in range(ny):
                data = np.float64(struct.unpack(">d", file.read(8))[0])
                dataset[n][i][j] = data
    for n in range(nlayers):
        binfile = open(str(int(v[n] * 1000)) + "vDIDV.bin", "wb")
        data = struct.pack(">i", nx)
        binfile.write(data)
        data = struct.pack(">i", ny)
        binfile.write(data)
        data = struct.pack(">d", v[n])
        binfile.write(data)
        data = struct.pack(">d", 0)
        binfile.write(data)

        for i in range(len(x)):
            data = struct.pack(">d", x[i])
            binfile.write(data)
        for i in range(len(y)):
            data = struct.pack(">d", y[i])
            binfile.write(data)

        for i in range(nx):
            for j in range(ny):
                data = struct.pack(">d", dataset[n][i][j])
                binfile.write(data)
        binfile.close()
def read_java_bin_single_layer(filepath):
    file = open(filepath,"rb")
    nx=struct.unpack(">i",file.read(4))[0]
    ny=struct.unpack(">i",file.read(4))[0]
    v=np.float64(struct.unpack(">d",file.read(8)))[0]
    current=np.float64(struct.unpack(">d",file.read(8)))[0]
    topo=np.zeros((nx,ny),dtype=np.float64)
    x=np.zeros(nx,dtype=np.float64)
    y=np.zeros(ny,dtype=np.float64)
    for i in range(nx):
        x[i] = np.float64(struct.unpack(">d", file.read(8)))[0]
    for j in range(nx):
        y[i] = np.float64(struct.unpack(">d", file.read(8)))[0]

    for i in range(nx):
        for j in range(ny):
            topo[i][j] = np.float64(struct.unpack(">d", file.read(8)))[0]
    dirname, basename = os.path.split(filepath)
    return topo,dirname
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