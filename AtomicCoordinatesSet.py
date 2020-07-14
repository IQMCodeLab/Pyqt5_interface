import math
import numpy as np
import Matrix
#import fieldops
import copy
path = 'C:/data/1/rawdata/Ufield'
"""
class AtomicCoordinatesSet
List of para:
ca:两个像素之间的夹角余弦值
alpha:两个点之间的夹角
beta:夹角的补角

"""
"""
AtomicCoordinatesSet:的意思：
首先，我们通过计算出晶格矢量(a1,b1)(a2,b2)，然后计算出pixel的矢量(x-center，y-center)
使用向量分解方法：
a1*x+a2*y = x-center
b1*x+b2*y = y-center
得出原子位置(x,y)
得到原子位置后，如果我们具有一个新的晶格矢量(修改后的)
那么这个时候，就可以得到原子在新的晶格矢量中的pixel。
"""

class AtomicCoordinatesSet:
    def __init__(self,a,b,origin):
        self.a = a
        self.b = b
        self.origin = np.empty(2)
        self.origin = origin
        self.am = math.sqrt(self.a[0]**2+self.a[1]**2)
        self.bm = math.sqrt(self.b[0]**2+self.b[1]**2)
        self.ca = self.dot(a,b)/(self.am*self.bm)
        self.alpha = math.acos(self.ca)
        self.beta = math.pi - self.alpha
        self.sa = math.sin(self.alpha)
        self.aHat = self.a/self.am
        self.bHat = self.b/self.bm
        self.dotHatbHat = self.dot(self.aHat,self.bHat)
        self.tempProja = np.empty(2)#a的投影
        self.tempProjb = np.empty(2)#b的投影
        self.tempReja = np.empty(2)
        self.tempRejb = np.empty(2)
        print(self.origin)
    def dot(self,a,b):
        return a[0]*b[0] + a[1]*b[1]

    def putAtomicCoordsVectors(self,pixX,pixY,atompt):
        self.temp = np.empty(2)
        self.temp[0] = pixX
        self.temp[1] = pixY
        '''
        self.tda = self.dot(self.temp,self.aHat)
        self.tdb = self.dot(self.temp,self.bHat)
        self.tempProja[0] = self.tda*self.aHat[0]
        self.tempProja[1] = self.tda*self.aHat[1]
        self.tempProjb[0] = self.tdb*self.bHat[0]
        self.tempProjb[1] = self.tdb*self.bHat[1]
        self.tempReja[0] = self.temp[0] - self.tempProja[0]
        self.tempReja[1] = self.temp[1] - self.tempProja[1]
        self.tempRejb[0] = self.temp[0] - self.tempProjb[0]
        self.tempProjb[1] = self.temp[1] - self.tempProjb[1]
        self.trdb = self.dot(self.tempReja,self.bHat)
        self.trda = self.dot(self.tempRejb,self.aHat)
        atompt[0] = self.trda/(self.am*self.sa*self.sa)
        atompt[1] = self.trdb/(self.bm*self.sa*self.sa)
        '''
        atompt[1] = (self.temp[0]*self.a[1] - self.temp[1]*self.a[0])/(self.a[1]*self.b[0]-self.b[1]*self.a[0])
        atompt[0] = (self.temp[1]*self.b[0]-self.temp[0]*self.b[1])/(self.a[1]*self.b[0]-self.b[1]*self.a[0])
        return atompt
    def putAtomicCoords(self,pixx,pixy,atompt):
        return self.putAtomicCoordsVectors(pixx-self.origin[0],pixy-self.origin[1],atompt)
    @staticmethod
    def generateCentered_static(bragg, N):
        latticeVectors = np.empty((2,2))
        for i in range(2):
            a = int((i+1)%2)
            latticeVectors[i][0] = - bragg[a][1]
            latticeVectors[i][1] = bragg[a][0]
            m = math.sqrt(latticeVectors[i][0] ** 2 + latticeVectors[i][1] ** 2)
            for j in range(2):
                latticeVectors[i][j] /= m
            dot = latticeVectors[i][0] * bragg[i][0] + latticeVectors[i][1] * bragg[i][1]
            for j in range(2):
                latticeVectors[i][j] *= (N / dot)
        print("latticVector({},{}),({},{})".format(latticeVectors[0][0],latticeVectors[0][1],latticeVectors[1][0],latticeVectors[1][1]))
        return AtomicCoordinatesSet(latticeVectors[0], latticeVectors[1], [N / 2, N / 2])
    @staticmethod
    def generateCentered_piexl(bragg, N):
        latticeVectors = np.empty((2, 2))
        braggTrue = np.empty((2,2))
        braggTrue = bragg*2*math.pi/N
        for i in range(2):
            latticeVectors[i][0] = -braggTrue[int((i + 1) % 2)][1]
            latticeVectors[i][1] = braggTrue[int((i + 1) % 2)][0]
            m = math.sqrt(latticeVectors[i][0] ** 2 + latticeVectors[i][1] ** 2)
            for j in range(2):
                latticeVectors[i][j] /= m
            dot = latticeVectors[i][0] * braggTrue[i][0] + latticeVectors[i][1] * braggTrue[i][1]
            for j in range(2):
                latticeVectors[i][j] *= N / dot
        return AtomicCoordinatesSet(latticeVectors[0], latticeVectors[1], [N / 2, N / 2])

    def getAtomicCoords(self,pixX,pixY):
        atomPt = np.empty(2)
        return self.putAtomicCoords(pixX,pixY,atomPt)
    def getPixelCoords(self,at):
        ans = np.empty(2)
        return self.putPixelCoords(at[0],at[1],ans)
    def putPixelCoords(self,atx,aty,ans):
        ans[0] = atx*self.a[0] + aty*self.b[0] + self.origin[0]
        ans[1] = atx*self.a[1] + aty*self.b[1] + self.origin[1]
        return ans
    def getReciprocalLattice(self):
        rVec =np.array([[self.b[1],-self.b[0]],[self.a[1],-self.a[0]]])
        dota = AtomicCoordinatesSet.dot(rVec[0],self.a)
        dotb = AtomicCoordinatesSet.dot(rVec[1],self.b)
        for i in range(2):
            rVec[0][i] *=(2*math.pi/dota)
            rVec[1][i] *=(2*math.pi/dotb)
        print("reciprocipallattice({},{}),({},{})".format(rVec[0][0],rVec[0][1],rVec[1][0],rVec[1][1]))
        return AtomicCoordinatesSet(rVec[0],rVec[1],copy.deepcopy(self.origin))

    @staticmethod
    def dot(a,b):
        return a[0]*b[0]+a[1]*b[1]

    """
    def generateCentered(bragg,N):
        latticeVectors = np.empty((2,2))
        for i in range(2):
            latticeVectors[i][0] =-bragg[int((i+1)%2)][1]
            latticeVectors[i][1] = bragg[int((i+1)%2)][0]
            m = math.sqrt(latticeVectors[i][0]**2+latticeVectors[i][1]**2)
            dot = AtomicCoordinatesSet.dot(latticeVectors[i],bragg[i])
            for j in range(2):
               latticeVectors[i][j] = latticeVectors[i][j]*N/dot
        return AtomicCoordinatesSet(latticeVectors[0],latticeVectors[1],np.array([N/2,N/2]))
    """


