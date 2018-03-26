# -*- coding: utf-8 -*
from numpy import *

def loadData():
    dataMatrix = mat([[1.,2.1],
    [2,1.1],
    [1.3,1.],
    [1.,1.],
    [2.,1.]])
    dataLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataMatrix,dataLabels

def loadDataSet(filename):
    # feature_num = len(open(filename).readline().split('\t'))
    fp = open(filename)
    datamat = []
    datalabel = []
    for line in fp.readlines():
        datamat.append(line.strip().split('\t')[:,-1])
        datalabel.append(line.strip().split('\t')[-1])
    return datamat,datalabel

def stumpClassify(datamatrix, i, threshold, inequal): #
    predictedVals = ones((shape(datamatrix)[0], 1))
    if inequal == 'lt':
        predictedVals[datamatrix[:,i] <= threshold] = -1.0
    else:
        predictedVals[datamatrix[:,i] > threshold] = 1.0
    return predictedVals #返回某个阈值下估计的输出

def buildstump(data, labels, D): #返回利用D得到的具有最小错误率的单层决策树，以及最小的错误率和g估计的类别向量
    datamatrix = mat(data)
    labels = mat(labels).T
    m,n = shape(datamatrix)
    numStep = 10.0 #训练次数
    bestStump = {}
    bestclassEst = mat(zeros((m,1)))
    minError = inf #初始化错误数量为∞
    for i in range(n):  #每一次迭代一个特征
        dataMin = min(datamatrix[:,i])
        dataMax = max(datamatrix[:,i])
        stepSize = (dataMax - dataMin)/numStep
        for j in range(-1, int(numStep)+1):
            for inequal in ['lt','gt']:  #比阈值小或大 less than or greater than
                threshold = (dataMin + float(j)*stepSize) #设置阈值，每次阈值加一个步长
                predictedVal = stumpClassify(datamatrix, i, threshold, inequal)
                err = mat(ones((m,1)))
                # import ipdb; ipdb.set_trace()
                err[predictedVal == labels] = 0
                weightedError = D.T*err
                # print "split: dim %d, threshold %2f, threshold inequal: %s, weightedError %3f" % (i, threshold, inequal, weightedError)
                if weightedError < minError:
                    minError = weightedError
                    bestclassEst = predictedVal.copy()
                    bestStump['dim'] = i
                    bestStump['threshold'] = threshold
                    bestStump['inequal'] = inequal
    return bestStump,minError,bestclassEst #返回最佳的单层决策树信息

def adaboostTrainDS(data, labels, numIt=40): #迭代次数40次
    weakClassArr = []
    m = shape(data)[0]
    D = mat(ones((m,1))/m)
    aggClassEst = mat(zeros((m,1))) #记录每个数据点的类别估计累计值
    for i in range(numIt):
        bestStump,minError,bestclassEst = buildstump(data, labels, D)
        print "D:",D.T
        alpha = float(0.5*log((1.0-minError)/max(minError,1e-16)))
        bestStump['alpha'] = alpha
        print "alpha:",alpha
        weakClassArr.append(bestStump)
        print "classEst: ",bestclassEst.T
        expon = multiply(-1*alpha*mat(labels).T, bestclassEst)
        D = multiply(D, exp(expon))
        D = D/D.sum()
        aggClassEst += alpha*bestclassEst
        print "aggClassEst: ",aggClassEst.T
        aggErrors = multiply(sign(aggClassEst) != mat(labels).T,ones((m,1)))
        errRate = aggErrors.sum()/m
        print "total error: ",errRate,"\n"
        if errRate == 0:
            break
    return weakClassArr

def adaClassify(data, classifierArr): #测试数据
    dataMatrix = mat(data)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['threshold'], classifierArr[i]['inequal'])
        aggClassEst += classifierArr[i]['alpha']*classEst
        print aggClassEst
    return sign(aggClassEst)
