import numpy as np
import scipy
import math
import fieldops
import Get_Bragg_Point
import Mask
import AtomicCoordinatesSet
import copy
import sys
sys.path.append("C:/Users/吴平/source/repos/Pybind11_test/x64/Release")
import binaryfile_read_write as wrb
import sys
sys.path.append("C:/Users/吴平/source/repos/My_Project/x64/Release")
import Pybind11_test
path = 'C:/data/1/rawdata/Ufield'
'''
doc for UfieldCalculationReal
stopEarly 
Topo:形貌图数据
angle:两个Bragg点间的角度
nlayers:计算u的层数。通过nlayers控制计算mask的宽度
fancy:是否选择使用fft-ifft方法施加u
'''
class UFieldCalculationReal:
    def __init__(self,stopEarly,Topo,angle,bragg,nlayers,fancy):
        self.fancy = fancy
        self.stopEarly = stopEarly
        self.source = Topo
        self.placetoputTranslation = np.empty(2)
        self.angle = angle
        self.nlayers = nlayers
        self.bragg = bragg
        self.len_x = np.shape(self.source)[0]
        self.len_y = np.shape(self.source)[1]
        self.n = self.len_x
        self.braggTrue = self.getBraggTrue(self.bragg,self.n)
        print("实际Bragg点为")
        print(self.braggTrue)
        self.latt = AtomicCoordinatesSet.AtomicCoordinatesSet(self.braggTrue[0],self.braggTrue[1],np.array([self.n/2,self.n/2])).getReciprocalLattice()
        self.expU = np.empty((self.len_y,self.len_x,2))
        self.expUPhase = np.empty((2,self.len_y,self.len_x))
        self.phaseN = np.empty((2,self.len_y,self.len_x))
        self.phaseCont  = np.empty((self.nlayers,2,self.len_y,self.len_x))
        self.U = np.empty((self.len_y,self.len_x,2))
        self.after = np.empty((self.len_y,self.len_x))
        self.ureg = np.empty((self.len_y,self.len_x,2))
        self.phaseTopo = np.empty((2,self.len_y,self.len_x,2))
        self.unitlength =self.len_x/fieldops.distance(self.bragg[0][0],self.bragg[0][1])
        if self.nlayers >1:
            self.maxLenghth = self.unitlength*math.sqrt(4*self.nlayers)
        else:
            self.maxLenghth = self.unitlength
        self.energy = np.empty(self.nlayers)
        #self.lengths = np.linspace(0,self.maxLenghth,self.nlayers,dtype=float)
        self.lengths = fieldops.generateArrayNotInclLower(0,self.maxLenghth,self.nlayers)
        print('GaussMask的宽度分别为{}'.format(self.lengths))
        self.reg = Get_Bragg_Point.BraggVectorRegularizer(self.angle,self.n,self.bragg[0][0] %2 == 0 or self.bragg[0][1] %2 == 0 or self.bragg[1][0] %2 == 0 or self.bragg[1][1] %2 == 0)
        self.doSummation()
    '''
    @getBraggTrue:计算将像素位置转换为理论位置
    '''
    def getBraggTrue(self, bragg, n):
        ans = np.empty((2,2))
        for i in range(2):
            for j in range(2):
                ans[i][j] = bragg[i][j]*2*math.pi/n

        return ans
    '''
    @doSummation
    '''
    def doSummation(self):
        for i in range(2):
            for j in range(self.n):
                for k in range(self.n):
                    '''
                    self.phaseTopo[i][k][j][0] = math.cos(fieldops.dot(self.braggTrue[i],j,k))*self.source[k][j]
                    self.phaseTopo[i][k][j][1] = math.sin(fieldops.dot(self.braggTrue[i],j,k))*self.source[k][j]
                    '''
                    self.phaseTopo[i][j][k][0] = math.cos(fieldops.dot(self.braggTrue[i],j,k))*self.source[j][k]
                    self.phaseTopo[i][j][k][1] = -math.sin(fieldops.dot(self.braggTrue[i],j,k))*self.source[j][k]

    '''
    @doExpUCalc
    '''
    def doExpUCalc(self):
        for j in range(self.nlayers):
            for i in range(2):
                print('现在正在计算第{}层,第{}个bragg点'.format(j+1,i))
                gaussMask = Mask.getGaussianMask(self.lengths[j])
                self.expU = fieldops.getDeviationGaussianDefault(self.lengths[j],self.phaseTopo[i],gaussMask)
                #self.expU = Pybind11_test.getDeviationGaussDefault(self.lengths[j], self.phaseTopo[i], gaussMask)
               # self.expU = applymask.getDeviationGaussianDefault(self.lengths[j],self.phaseTopo[i],gaussMask)
                '''
                for  m  in range(self.n):
                    for n in range(self.n):
                '''
                #expU_Complex = np.empty((self.len_x,self.len_y),dtype=complex)
               # expU_Complex = self.expU[:,:,0]+1j*self.expU[:,:,1]
               # self.expUPhase[i,:,:] = np.angle(expU_Complex)+math.pi
                self.expUPhase[i,:,:] = fieldops.atan_for_array(self.expU[:,:,0],self.expU[:,:,1])
                #self.expUPhase[i,:,:] = np.arctan(self.expU[:,:,1]/self.expU[:,:,0])
                self.phaseN[i] = fieldops.putPhaseSteps(self.expUPhase[i,:,:],int(self.n/2),int(self.n/2))
                self.phaseCont[j][i] = fieldops.putAddedPhaseSteps(self.expUPhase[i,:,:],self.phaseN[i,:,:],2*math.pi)
                #print(self.phaseCont)
                self.phaseCont[j][i] = fieldops.substractAvg(self.phaseCont[j][i])
    '''
    @getEnergy 计算我们计算出来的数据的正确性
    '''
    def getEnergy(self,phaseCont):
        energy = 0
        len_x = np.shape(phaseCont[0])[1]
        for i in range(2):
            energy += fieldops.getNlargeDifferences(phaseCont[i,:,:],math.pi/4)
            energy -= np.sum(fieldops.gradMag(phaseCont[i,:,:]))/(math.pi*len_x*len_x)
        return energy
    '''
    pickBestLayer: 选择能量最小的Mask宽度作为我们的层数
    '''
    def pickBestlayer(self):
        for i in range(self.nlayers):
            self.energy[i] = self.getEnergy(self.phaseCont[i])
        self.selectlayer = np.argmin(self.energy)
        print('能量序列为')
        print(self.energy)
        print('我们选择的是第{}层'.format(self.selectlayer+1))
    '''
    @makeBestUfield:计算最好层数的能量
    '''
    def makeBestUfield(self):
        self.U=fieldops.putU(self.phaseCont[self.selectlayer,0,:,:],self.phaseCont[self.selectlayer,1,:,:],self.braggTrue,1)

    '''
    对我们的Bragg点做矫正
    '''
    def doRegularization(self):
        self.reg.setFirstBraggPeak(self.braggTrue[0,:])
        self.reg.setSecondBraggPeak(self.braggTrue[1,:])
        self.reg.regularize()
        self.lattReg = self.reg.getRegLattice()
        self.braggReg = self.reg.getFinalBragg()
        print("最终的bragg点为({},{}),({},{})".format(self.braggReg[0][0],self.braggReg[0][1],self.braggReg[1][0],self.braggReg[1][1]))
        self.ureg = fieldops.putUField(self.latt,self.lattReg,copy.deepcopy(self.ureg))
    def applyUfield(self):
        if self.fancy:
            self.after = fieldops.applyUFieldSpecial_withShifting(self.UCombine,self.source,self.braggReg,self.placetoputTranslation)
            outsidePixels = fieldops.getOutsidePixels(self.UCombine)
            after = fieldops.zero(self.after,outsidePixels)
            self.after = fieldops.changezerotoaverage(after)
        return self.after
    def addReglarization(self):
        self.UCombine = self.U + self.ureg
    def apply_U_Field(self):
        if self.fancy:
            self.after = fieldops.applyUFieldSpecial_withShifting(self.ureg,self.source,self.braggReg,self.placetoputTranslation)
            outsidePixels = fieldops.getOutsidePixels(self.ureg)
            self.after = fieldops.zero(self.after,outsidePixels)
            self.after = fieldops.changezerotoaverage(self.after)
        return self.after