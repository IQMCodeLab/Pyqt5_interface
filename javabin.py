import numpy as np
import matplotlib.pyplot as plt
import struct
import os
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
    return dataset,v
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
    dirname,basename = os.path.split(filepath)
    nx=struct.unpack(">i",file.read(4))[0]
    ny=struct.unpack(">i",file.read(4))[0]
    v=np.float64(struct.unpack(">d",file.read(8)))[0]

    current=np.float64(struct.unpack(">d",file.read(8)))[0]
    print(struct.pack('>d', current))

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
    return topo,dirname