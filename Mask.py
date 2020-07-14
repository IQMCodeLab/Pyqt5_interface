import math
import numpy as np
import scipy
import fieldops
"""
这个函数相当于一个截断的高斯分布，首先x相当于标准差。

"""
def getGaussianMask(x):
    L = int(round(4*x+2))
    print("截断长度为{}".format(L))
    g_one_axis = np.empty(L,dtype=float)
    g = np.empty((L,L),dtype=float)
    for i  in range(L):
        for j in range(L):
            d = fieldops.distance(i,j)
            g[i][j] = math.exp(-(d*d)/(x*x))
    sigma = math.sqrt(2)*x
    for i in range(L):
        g_one_axis[i] = math.exp(-i**2/(2*x**2))

    return g
