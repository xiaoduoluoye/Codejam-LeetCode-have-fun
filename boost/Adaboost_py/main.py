# -*- coding: utf-8 -*

from Adaboost_py import *
import matplotlib.pyplot as plt
from numpy import *
import ipdb
from mpl_toolkits.mplot3d import Axes3D


Data,Labels = loadData()
# plt.plot(Data[0],Data[1],'*')
# plt.show()
# bestStump,minError,bestclassEst = buildstump(Data, Labels, D)
classifierArray = adaboostTrainDS(Data,Labels,9)
# ipdb.set_trace()
print adaClassify([[0,0],[9,9],[-1,0],[1,2],[-2,-2]],classifierArray)
