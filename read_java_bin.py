import numpy as np
import struct

def read_java_bin_file(Filepath):

    print(Filepath)
    # Filepath="D:/dan Java/3ds/316Z_flat.bin"
    file = open(Filepath, "rb")

    nx = struct.unpack(">i", file.read(4))[0]
    ny = struct.unpack(">i", file.read(4))[0]

    print(nx)
    print(ny)
    print(struct.pack('>i',nx))

    v = np.float64(struct.unpack(">d", file.read(8)))[0]
    current = np.float64(struct.unpack(">d", file.read(8)))[0]

    data = np.zeros((nx, ny), dtype=np.float64)
    x = np.zeros(nx, dtype=np.float64)
    y = np.zeros(ny, dtype=np.float64)

    for i in range(nx):
        x[i] = np.float64(struct.unpack(">d", file.read(8)))[0]
    for j in range(nx):
        y[i] = np.float64(struct.unpack(">d", file.read(8)))[0]

    for i in range(nx):
        for j in range(ny):
            data[i][j] = np.float64(struct.unpack(">d", file.read(8)))[0]
    return  data

def read_txt_file(path):
    import re
    file = open(path,'r',encoding='utf-8')
    list_arr = file.readlines()
    lists = []
    r = '[’!"#$%&\'()*+,/:;<=>?@[\\]^_`{|}~]'
    for index, x in enumerate(list_arr):
        a = re.sub(r,'',x)
        c = a.strip()
        c = c.split()
        lists.append(c)
    return np.array(lists)
"""
def write_txt_file(data):
"""