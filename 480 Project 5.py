import random as r
#import numpy as np #for argmax in multiclass perceptron
def features(x, N, M): #input NxM image(2d aray [N][M]) x, output length 6 feature array
    # 1)
    Density = sum(x)/(N*M)
    # 2)
    for i in range(N):
        for j in range(M):
            DOFS += x[i][j] ^ x[j][i]
    DOFS /= (N*M)
    # 3,4,5,6)
    BW = [[0]*M]*N #initialize a new NxM array
    for i in range(N):
        for j in range(M):
            BW[i][j] = int(x[i][j]<=128)#thresholding operation
    # 3,4)
    Cols = []
    # 5,6)
    Rows = []
    # 3,4)
    for i in range(N): #find number of changes between 0 and 1, for columns
        p = BW[i][0]
        count = 0
        for j in range(M): #Column Major
            if(p != BW[i][j]):
                count += 1
                p =BW[i][j]
        Cols.append(count)
    # 5,6)
    for j in range(M): #find number of changes between 0 and 1, for rows
        p = BW[0][j]
        count = 0
        for i in range(N): #Row Major
            if(p != BW[i][j]):
                count += 1
                p =BW[i][j]
        Rows.append(count)
    # 3)
    maxInterHoriz = max(Cols)
    # 4)
    aveInterHoriz = sum(Cols)/len(Cols)
    # 5)
    maxInterVert = max(Rows)
    # 6)
    aveInterVert = sum(Rows)/len(Rows)
    return [0, Density, DOFS, maxInterHoriz, aveInterHoriz, maxInterVert, aveInterVert]
    #order: [Bias, Density, Degree/Measure of Symettry, maximum horizontal intersections, average horizntal intersections, maximum vertical intersections, average vertical intersections]

class Perceptron:
    def __init__(self):
        self.W = [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)]
    def pTrain(self, inp, L, O, n ): #where L is [0,1]
        for a in range(len(self.W)):
            self.W[a] = self.W[a] + n*(O-L)*inp[a]
    def pProcess(self, x):
        temp = 0
        for a in range(len(self.W)):
            temp += x[a]*self.W[a]
        return int(temp > 0)
    def getWeights(self):
        return self.W

class MultiPerceptron:
    def __init__(self):
        self.W = [[(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#0
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#1
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#2
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#3
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#4
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#5
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#6
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#7
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)],#8
                  [(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10),(((r.random()*2)-1)/10)]]#9
    def pTrain(self, inp, L, O, n ): #where L is the label[0,9], O is the label the neuron guessed, inp is the input, n is eta
        for a in range(len(self.W[L])):
            self.W[L][a] = self.W[L][a] + n*inp[a]
        for a in range(len(self.W[L])):
            self.W[O][a] = self.W[O][a] - n*inp[a]
    def pProcess(self, x):
        tomp = []
        for a in range(len(self.W)):
            temp = 0
            for b in range(len(self.W[a])):
                temp += x[b]*self.W[a][b]
            tomp.append(temp)
        return tomp.index(max(tomp))
    def getWeights(self):
        return self.W
class NNwrk:
