import numpy as np
import math
def putRotationMatrix(theta):
    matrix = np.empty((2,2))
    matrix[0][0] = math.cos(theta)
    matrix[0][1] = math.sin(theta)
    matrix[1][0] = -math.sin(theta)
    matrix[1][1] = math.cos(theta)
    return matrix
def getProductWith(mat,vec):
    ans = putProductWith(mat,vec)
    return ans
def putProductWith(mat,vec):
    ans = np.empty(2)
    ans[0] =mat[0][0]*vec[0]+mat[1][0]*vec[1]
    ans[1] = mat[0][1]*vec[0]+mat[1][1]*vec[1]
    return ans
