import numpy as np
import math
import scipy
import sys

sys.path.append("C:/Users/吴平/source/repos/Pybind11_test/x64/Release")
from scipy.ndimage import gaussian_filter
from scipy import fftpack, signal
import copy
import operator
from functools import reduce
import Pybind11_test

path = 'C:/data/1/rawdata/Ufield'
import AtomicCoordinatesSet
from scipy import linalg
import binaryfile_read_write as wrb


def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def mag(a):
    """
    :param a:
    :return:
    """
    return math.sqrt(a[0] ** 2 + a[1] ** 2)


def unitvector(a):
    """
    :param a:
    :return:
    """
    new_array = a / mag(a)
    return new_array


def phase(a):
    """
    :param a:
    :return:
    """
    return atan(a[0], a[1])


def roundEven(x):
    """
    :param x:
    :return:
    """
    return round(x / 2) * 2


def round(x):
    """
    :param x:
    :return:
    """
    return int(x + 100000000000 + 0.5) - 100000000000


def getDeviationGaussianDefault(L, cosmsintopo, gauss):
    """
    尝试使用高斯滤波器，可以减少运算时间,新的算法中，是在C++中写出了这个程序，然后调用
    :param L:
    :param cosmsintopo:
    :param gauss:
    :return:
    """
    len_x = int(np.shape(cosmsintopo)[1])
    len_y = int(np.shape(cosmsintopo)[0])
    cmplex = np.empty(2)
    gsum = 0
    expu = np.empty((len_x, len_y, 2))
    sigma_x = L / math.sqrt(2)
    print("标准差为{}".format(sigma_x))
    expu[:, :, 0] = gaussian_filter(cosmsintopo[:, :, 0], sigma=sigma_x, truncate=4.0)
    expu[:, :, 1] = gaussian_filter(cosmsintopo[:, :, 1], sigma=sigma_x, truncate=4.0)
    return expu


def putPhaseSteps(phase, sx, sy):
    '''
    :param phase:
    :param sx:
    :param sy:
    :return:
    '''
    p = 2 * math.pi
    len_x, len_y = np.shape(phase)
    print(sx, sy)

    visited = np.empty((len_x, len_y), dtype=bool)
    for i in range(len_x):
        for j in range(len_y):
            visited[i][j] = False
    n = np.empty((len_x, len_y))
    visited[sx][sy] = True
    queue = np.array([
        [sx, sy, sx + 1, sy],
        [sx, sy, sx - 1, sy],
        [sx, sy, sx, sy + 1],
        [sx, sy, sx, sy - 1]])

    counter = 0

    while queue.size > 0:
        counter = counter + 1
        points = queue[0]
        queue = np.delete(queue, obj=0, axis=0)
        visited[points[2]][points[3]] = True
        if abs(phase[points[0]][points[1]] - phase[points[2]][points[3]]) < p / 4:
            n[points[2]][points[3]] = n[points[0]][points[1]]
        elif phase[points[0]][points[1]] > phase[points[2]][points[3]]:
            n[points[2]][points[3]] = n[points[0]][points[1]] + 1
        else:
            n[points[2]][points[3]] = n[points[0]][points[1]] - 1

        if points[2] > 0 and not visited[points[2] - 1][points[3]]:
            queue = np.append(queue, [[points[2], points[3], points[2] - 1, points[3]]], axis=0)
            visited[points[2] - 1][points[3]] = True
        if points[3] > 0 and not visited[points[2]][points[3] - 1]:
            queue = np.append(queue, [[points[2], points[3], points[2], points[3] - 1]], axis=0)
            visited[points[2]][points[3] - 1] = True
        if points[2] < len_x - 1 and not visited[points[2] + 1][points[3]]:
            queue = np.append(queue, [[points[2], points[3], points[2] + 1, points[3]]], axis=0)
            visited[points[2] + 1][points[3]] = True
        if points[3] < len_x - 1 and not visited[points[2]][points[3] + 1]:
            queue = np.append(queue, [[points[2], points[3], points[2], points[3] + 1]], axis=0)
            visited[points[2]][points[3] + 1] = True
    print("我们计算了{}次".format(counter))
    return n


def phaseStep(phase, points, p, n):
    """
    :param phase:
    :param points:
    :param p:
    :param n:
    :return:
    """
    if abs(phase[points[0]][points[1]] - phase[points[2]][points[3]]) < p / 4:
        n[points[2]][points[3]] = n[points[0]][points[1]]
    elif phase[points[0]][points[1]] > phase[points[2]][points[3]]:
        n[points[2]][points[3]] = n[points[0]][points[1]] + 1
    else:
        n[points[2]][points[3]] = n[points[0]][points[1]] - 1
    return n


def putAddedPhaseSteps(phase, n, p):
    """
    :param phase:
    :param n:
    :param p:
    :return:
    """
    print(n)
    target = phase + n * p
    return target
    '''
    计算相位的平均值
    '''


def substractAvg(data):
    """
    :param data:
    :return:
    """
    len_y, len_x = np.shape(data)
    mean_data = np.mean(data)
    data_new = data - mean_data
    return data_new
    '''
    @getNlargerDifference 
    计算能量
    '''


def getNlargeDifferences(f, threshold):
    """
    :param f:
    :param threshold:
    :return:
    """
    ans = 0
    nx, ny = np.shape(f)
    if math.fabs(f[0][0] - f[0][1]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[0][0] - f[1][0]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[nx - 1][0] - f[nx - 1][1]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[nx - 1][0] - f[nx - 2][0]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[0][ny - 1] - f[0][ny - 2]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[0][ny - 1] - f[1][ny - 1]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[nx - 1][ny - 1] - f[nx - 1][ny - 2]) > threshold:
        ans += 1
    else:
        pass
    if math.fabs(f[nx - 1][ny - 1] - f[nx - 2][ny - 1]) > threshold:
        ans += 1
    else:
        pass
    for i in range(1, ny - 1):
        if math.fabs(f[1][i] - f[0][i]) > threshold:
            ans + 1
        else:
            pass
        if math.fabs(f[nx - 1][i] - f[nx - 2][i]) > threshold:
            ans = ans + 1
        else:
            pass
    for i in range(1, nx - 1):
        if math.fabs(f[i][1] - f[i][0]) > threshold:
            ans = ans + 1
        else:
            pass
        if math.fabs(f[i][ny - 1] - f[i][ny - 2]) > threshold:
            ans = ans + 1
        else:
            pass
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            if math.fabs(f[i][j] - f[i + 1][j]) > threshold:
                ans = ans + 1
            else:
                pass
            if math.fabs(f[i][j] - f[i - 1][j]) > threshold:
                ans = ans + 1
            else:
                pass
            if math.fabs(f[i][j] - f[i][j + 1]) > threshold:
                ans = ans + 1
            else:
                pass
            if math.fabs(f[i][j] - f[i][j - 1]) > threshold:
                ans = ans + 1
            else:
                pass
    return ans


def gradMag(data):
    """
    :param data:
    :return:
    """
    grad = gradientNM2(data)
    return magnitude(grad)


def gradientNM2(field):
    """
    :param field:
    :return:
    """
    nx, ny = np.shape(field)
    grad = np.empty((nx, ny, 2))

    for i in range(ny):
        grad[0][i][0] = field[1][i] - field[0][i]
        grad[nx - 1][i][0] = field[nx - 1][i] - field[nx - 2][i]
    for i in range(nx):
        grad[i][0][1] = field[i][1] - field[i][0]
        grad[i][ny - 1][1] = field[i][ny - 1] - field[i][ny - 2]
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            grad[i][j][0] = (field[i + 1][j] - field[i - 1][j]) / 2
            grad[i][j][1] = (field[i][j + 1] - field[i][j - 1]) / 2
    return grad


def magnitude(f):
    """
    :param f:
    :return:
    """
    N, M, nz = np.shape(f)
    mag = np.empty((N, M))
    for i in range(N):
        for j in range(M):
            mag[i][j] = math.sqrt(f[i][j][0] * f[i][j][0] + f[i][j][1] * f[i][j][1])
    return mag


def product(a, b):
    return np.array([a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]])


def expmi(x):
    '''
    :param x:
    :return: 返回cos和sin值
    '''
    return np.array([math.cos(x), -math.sin(x)])
    '''
    @putU:
    '''


def putU(phasex, phasey, bragg, eta):
    '''
    :param phasex:
    :param phasey:
    :param bragg:
    :param eta:
    '''
    n = np.shape(phasex)[0]
    m = np.shape(phasex)[1]
    u = np.empty((n, m, 2))
    mags = np.empty(2)
    mags[0] = math.sqrt(bragg[0][0] ** 2 + bragg[0][1] ** 2)
    mags[1] = math.sqrt(bragg[1][0] ** 2 + bragg[1][1] ** 2)
    k1Hat = np.empty(2)
    k2Hat = np.empty(2)
    k1Hat[0] = bragg[0][0] / mags[0]
    k1Hat[1] = bragg[0][1] / mags[0]
    k2Hat[0] = bragg[1][0] / mags[1]
    k2Hat[1] = bragg[1][1] / mags[1]
    costh = k1Hat[0] * k2Hat[0] + k1Hat[1] * k2Hat[1]
    k2PrimeHat = np.empty(2)
    k2PrimeHat[0] = k2Hat[0] - costh * k1Hat[0]
    k2PrimeHat[1] = k2Hat[1] - costh * k1Hat[1]
    magPrime = math.sqrt(k2PrimeHat[0] ** 2 + k2PrimeHat[1] ** 2)
    k2PrimeHat /= magPrime
    for i in range(n):
        for j in range(m):
            udot1 = phasex[i][j] / mags[0]
            udot2 = phasey[i][j] / mags[1]
            udot2Prime = (udot2 - costh * udot1) / magPrime
            u[i][j][0] = eta * (udot1 * k1Hat[0] + udot2Prime * k2PrimeHat[0])
            u[i][j][1] = eta * (udot1 * k1Hat[1] + udot2Prime * k2PrimeHat[1])
    wrb.write_bin_with_name(path, u[:, :, 0], "U_x")
    wrb.write_bin_with_name(path, u[:, :, 1], "U_y")
    return u


def putUField(imperfect: AtomicCoordinatesSet.AtomicCoordinatesSet, perfect: AtomicCoordinatesSet.AtomicCoordinatesSet,u):
    """
    :param imperfect:
    :param perfect:
    :param u:
    :return:
    """
    coorImp = np.empty(2)
    pixPerf = np.empty(2)
    len_x = np.shape(u)[0]
    len_y = np.shape(u)[1]
    print(len_x, len_y)
    for i in range(len_x):
        for j in range(len_y):
            coorImp = imperfect.getAtomicCoords(i, j)
            pixPerf = perfect.getPixelCoords(coorImp)
            u[i][j][0] = pixPerf[0] - i
            u[i][j][1] = pixPerf[1] - j
    wrb.write_bin_with_name(path, u[:, :, 0], "uReg_x")
    wrb.write_bin_with_name(path, u[:, :, 1], "uReg_y")
    return u


def getRforTopo(source, fftz, bragg):
    """
    :param source:
    :param fftz:
    :param bragg:
    :return: the returns the position vector which should make the fft peak have the correct phase.
    """
    len_x = np.shape(fftz)[0]
    len_y = np.shape(fftz)[1]
    q = np.array([[2 * math.pi * bragg[0][0] / len_x, 2 * math.pi * bragg[0][1] / len_y],
                  [2 * math.pi * bragg[1][0] / len_x, 2 * math.pi * bragg[1][1] / len_y]])
    x1 = int((bragg[0][0] + len_x / 2) % len_x)
    y1 = int((bragg[0][1] + len_y / 2) % len_y)
    x2 = int((bragg[1][0] + len_x / 2) % len_x)
    y2 = int((bragg[1][1] + len_y / 2) % len_y)

    print("中心为({},{}),({},{})".format(x1, y1, x2, y2))
    phaseq1 = phasecenterzero(fftz[x1][y1])
    phaseq2 = phasecenterzero(fftz[x2][y2])
    """
    q代表的是Bragg点的位置，而phaseq1和phaseq2代表的是位于Bragg点的一个相位。LUDecomposition
    解决的可能是一个相位的偏差。
    """
    phase = np.array([phaseq1, phaseq2])
    print("phase为({},{})".format(phase[0], phase[1]))
    '''
    ans = linalg.lu_solve(q,phase)[0]
    '''
    ans = linalg.solve(q, phase)
    """
    LUDecomposition,就是他么的一个解线性方程组的方法。

    """
    print("输出R")
    print("{}+{}={}".format(ans[0], q[0][0], ans[0] * q[0][0]))
    print("{}+{}={}".format(ans[1], q[0][1], ans[1] * q[0][1]))
    print("{}+{}+{}+{}={}".format(ans[0], q[0][0], ans[1], q[0][1], ans[1] * q[0][1] + ans[0] * q[0][0]))
    print("{}+{}={}".format(ans[0], q[1][0], ans[0] * q[1][0]))
    print("{}+{}={}".format(ans[1], q[1][1], ans[1] * q[1][1]))
    print("{}+{}+{}+{}={}".format(ans[0], q[1][0], ans[1], q[1][1], ans[1] * q[1][1] + ans[0] * q[1][0]))
    return ans


def phasecenterzero(a):
    """
    :param a:
    :return:
    """
    if a[0] == 0:
        if a[1] > 0:
            return math.pi / 2
        else:
            return -math.pi / 2
    if a[0] > 0:
        return math.atan(a[1] / a[0])
    if a[1] > 0:
        return math.atan(a[1] / a[0]) + math.pi
    if a[1] < 0:
        return math.atan(a[1] / a[0]) - math.pi
    if a[1] == 0:
        return math.pi
    return 0


def changezerotoaverage(after):
    """
    :param after:
    :return:
    """
    after_1 = reduce(operator.add, after)
    non_zero = [v for v in after_1 if v != 0]
    average = np.sum(non_zero) / np.shape(non_zero)[0]
    for i in range(np.shape(after)[0]):
        for j in range(np.shape(after)[1]):
            if after[i][j] == 0:
                after[i][j] = average
    return after


def pluseequal(ansre, mean):
    """
    :param ansre:
    :param mean:
    :return:
    """
    ansre_new = ansre + mean
    return ansre_new


def translateFancy(source, fftz, r, periodic):
    """
    :param source:
    :param fftz:
    :param r:
    :param periodic:
    :return:
    """
    len_x = np.shape(fftz)[0]
    len_y = np.shape(fftz)[1]
    phase = np.empty((len_x, len_x))
    new_fftz = np.empty((len_x, len_y, 2))
    for i in range(len_x):
        qx = (i - len_x / 2) * 2 * math.pi / len_x
        for j in range(len_y):
            qy = (j - len_y / 2) * 2 * math.pi / len_y
            phase[i][j] = qx * r[0] + qy * r[1]
            new_fftz[i][j] = product(fftz[i][j], expmi(phase[i][j]))
    new_fftz = shift(new_fftz)
    new_fftz_1 = new_fftz[:, :, 0] + 1j * new_fftz[:, :, 1]
    wrb.write_bin_with_name(path, np.abs(new_fftz_1), "fftz_translateFancy")
    fftz_complex = new_fftz[:, :, 0] + 1j * new_fftz[:, :, 1]
    ans = np.fft.ifft2(fftz_complex)
    ans_real = np.real(ans)
    if periodic == False:
        for i in range(len_x):
            for j in range(len_y):
                if i - r[0] < 0 or i - r[0] > len_x - 1 or j - r[1] < 0 or j - r[1] > len_y - 1:
                    ans_real[i][j] = 0
    ans_new = changezerotoaverage(ans_real)
    return ans_new


def applyUFieldSpecial_withShifting(u, data, bragg, placetoputTranslation):
    """
    :param u:
    :param data:
    :param bragg:
    :param placetoputTranslation:
    :return:
    """
    len_y, len_x = np.shape(data)
    mean_source = np.mean(data)
    source = substractAvg(data)
    fftz = Pybind11_test.Fourier_transform_center(source, u)
    R = getRforTopo(None, fftz, bragg)
    ansre = translateFancy(None, fftz, R, False)
    ansre_new = pluseequal(ansre, mean_source)
    return ansre_new


def getEnergy(phaseCont):
    """
    :param phaseCont:
    :return:
    """
    energy = 0
    for i in range(2):
        energy = energy + getNlargeDifferences(phaseCont[i], math.pi / 4)
        energy = energy - np.sum(gradMag(phaseCont[i])) / (math.pi * np.shape(phaseCont[0])[0] ** 2)
    return energy


def getOutsidePixels(u):
    N = np.shape(u)[1]
    M = np.shape(u)[0]
    r = np.empty(2)

    outsize = np.empty((N, M), dtype=bool)
    for i in range(N):
        for j in range(M):
            r[0] = i
            r[1] = j
            a = r[0] - u[i][j][0]
            b = r[1] - u[i][j][1]
            if a >= 0 or a < N or b >= 0 or b < M:
                outsize[i][j] = False
            else:
                outsize[i][j] = True
    return outsize


def zero(x, doIt):
    len_x, len_y = np.shape(x)
    for i in range(len_x):
        for j in range(len_y):
            if doIt[i][j]:
                x[i][j] = 0
    return x


def dot(a, b0, b1):
    """
    :param a:
    :param b0:
    :param b1:
    :return: the innver productor
    """
    return a[0] * b0 + a[1] * b1


def generateArrayNotInclLower(min, max, npts):
    dm = (max - min) / npts
    a = np.empty(int(npts))
    for i in range(int(npts)):
        a[i] = min + (i + 1) * dm
    return a


def atan(x, y):
    """
    :param x:
    :param y:
    :return: the angle of tan(y/x)
    """
    if x == 0:
        if y > 0:
            return math.pi / 2
        else:
            return 3 * math.pi / 2
    if x < 0:
        return math.atan(y / x) + math.pi
    if y < 0:
        return math.atan(y / x) + math.pi * 2
    return math.atan(y / x)


def atan_for_array(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    len_x, len_y = np.shape(x)
    angle = np.empty((len_x, len_y))
    for i in range(len_x):
        for j in range(len_y):
            if x[i][j] == 0:
                if y[i][j] > 0:
                    angle[i][j] = math.pi / 2
                else:
                    angle[i][j] = 3 * math.pi / 2
            if x[i][j] < 0:
                angle[i][j] = math.atan2(y[i][j], x[i][j]) + math.pi
            if y[i][j] < 0:
                angle[i][j] = math.atan2(y[i][j], x[i][j]) + math.pi * 2
            angle[i][j] = math.atan2(y[i][j], x[i][j]) + math.pi * 2
    return angle


def shift(source):
    N = np.shape(source)[0]
    M = np.shape(source)[1]
    target = np.empty((N, M, 2))
    for i in range(N):
        for j in range(M):
            x = int((i + N / 2) % N)
            y = int((j + M / 2) % M)
            target[i][j][0] = source[x][y][0]
            target[i][j][1] = source[x][y][1]
    return target


def subtractMeanPlane(matrix):
    """
    input: 2D nparray of original topography
    output: 2D nparray of topo subtracted backgroud
    """
    xdim,ydim = matrix.shape
    coordMatrix = np.zeros((xdim*ydim,3))
    zVector = np.zeros(xdim*ydim)
    for i in range(xdim):
        for j in range(ydim):
            coordMatrix[i*xdim+j] = [i,j,1]
            zVector[i*xdim+j] = matrix[i,j]

    zVector = np.matrix(zVector)
    coordMatrix = np.matrix(coordMatrix)
    planeVector = (coordMatrix.T * coordMatrix).I * coordMatrix.T * zVector.T
    planeMatrix = np.zeros((xdim,ydim))

    for i in range(xdim):
        for j in range(ydim):
            planeMatrix[i,j] = i*planeVector[0]+j*planeVector[1]+planeVector[2]

    return(np.subtract(matrix,planeMatrix))

def detectNaN(data):
    len_x, len_y = np.shape(data)
    lists = []

    for i in range(len_x):
        for j in range(len_y):
            if math.isnan(data[i][j]):
                lists = np.append(lists, i)
            break
    print(lists)

    data_delect = np.delete(data, lists, axis=0)
    return data_delect
