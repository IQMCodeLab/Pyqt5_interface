import numpy as np
import math
import fieldops
import Matrix
import AtomicCoordinatesSet

path = 'C:/data/1/rawdata/Ufield'

"""
注意angle,我们输入的是个角度制
注意我们传进来的bragg点是pixel还是实际的Bragg点
"""
class BraggVectorRegularizer:
    def __init__(self, angle, N, regeven):

        self.angle = angle*math.pi/180
        self.N = N
        self.regeven = regeven
        self.rotMat = np.empty((2, 2))
        self.rotMatT = np.empty((2, 2))
        self.braggSetRot = np.empty((2, 2, 2))
        self.unitBraggSetRot = np.empty((2, 2, 2))
        self.finalBragg = np.empty((2, 2))
        self.rotMat = Matrix.putRotationMatrix(self.angle)
        self.rotMatT = Matrix.putRotationMatrix(-self.angle)

    def setFirstBraggPeak(self, bragg):
        """
        :param bragg:
        :return:
        """
        for i in range(2):
            self.braggSetRot[0][0][i] = bragg[i]
        self.braggSetRot[0][1] = Matrix.getProductWith(self.rotMat, bragg)

    def setSecondBraggPeak(self, bragg):
        """
        :param bragg:
        :return:
        """
        for i in range(2):
            self.braggSetRot[1][1][i] = bragg[i]
        self.braggSetRot[1][0] = Matrix.getProductWith(self.rotMatT, bragg)

    def regularize(self):
        mag1 = fieldops.distance(self.braggSetRot[0][0][0], self.braggSetRot[0][0][1])
        mag2 = fieldops.distance(self.braggSetRot[1][1][0], self.braggSetRot[1][1][1])
        magAvg = (mag1 + mag2) / 2
        print("mag1({}),mag2({}),magAvg({})".format(mag1,mag2,magAvg))

        for i in range(2):
            for j in range(2):
                self.unitBraggSetRot[i][j] = fieldops.unitvector(self.braggSetRot[i][j])
        angle1 = fieldops.phase(self.unitBraggSetRot[0][0])
        angle2 = fieldops.phase(self.unitBraggSetRot[1][0])
        if np.abs(angle1 - angle2) > math.pi:
            if angle1 > math.pi:
                angle1 = angle1 - 2 * math.pi
            elif angle2 > math.pi:
                angle2 = angle2 - 2 * math.pi
        angleAvg = (angle1 + angle2) / 2
        print("angle1({}),angle2({}),angleAvg({})".format(angle1,angle2,angleAvg))
        self.finalBragg[0][0] = magAvg * math.cos(angleAvg)
        self.finalBragg[0][1] = magAvg * math.sin(angleAvg)
        self.finalBragg[1][0] = magAvg * math.cos(angleAvg + self.angle)
        self.finalBragg[1][1] = magAvg * math.sin(angleAvg + self.angle)
        print("finalBragg({},{}),({},{})".format(self.finalBragg[0][0],self.finalBragg[0][1],self.finalBragg[1][0],self.finalBragg[1][1]))
        temp = np.empty((2, 2))
        if self.regeven:
            temp[0] = self.roundBraggIntEven(self.finalBragg[0], self.N)
            temp[1] = self.roundBraggIntEven(self.finalBragg[1], self.N)
        else:
            temp[0] = self.roundBraggInt(self.finalBragg[0], self.N)
            temp[1] = self.roundBraggInt(self.finalBragg[1], self.N)
        self.finalBragg_pixel = temp

    def roundBraggIntEven(self, vec, N):
        temp = vec*N/ (2 * math.pi)
        temp[0] = fieldops.roundEven(temp[0])
        temp[1] = fieldops.roundEven(temp[1])
        return temp

    def roundBraggInt(self, vec, N):
        temp = vec*N/ (2 * math.pi)
        temp[0] = fieldops.round(temp[0])
        temp[1] = fieldops.round(temp[1])
        return temp

    def getFinalBragg(self):
        ans = np.empty((2, 2))
        for i in range(2):
            for j in range(2):
                ans[i][j] = fieldops.round(self.finalBragg_pixel[i][j])
        return ans

    def getRegLattice(self):
        return AtomicCoordinatesSet.AtomicCoordinatesSet.generateCentered_static(self.finalBragg_pixel, self.N)