__author__ = 'andy'
import os
import random

def getPathM():
    fileName = os.path.realpath(__file__)
    filePath = os.path.dirname(fileName)
    return filePath

# http://www.careercup.com/question?id=5398298810646528
def randRepData():
    a = []
    for i in range(500):
        a += [i] * random.randint(0, 499)
    random.shuffle(a)
    return a

#randRepData()
#print(randRepData())

def lambdaTest():
    cng = lambda j: j+1
    i = 1
    print(i)
    b, c = cng(i)



