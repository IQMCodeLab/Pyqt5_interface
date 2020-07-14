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
