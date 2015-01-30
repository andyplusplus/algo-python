__author__ = 'andy'
import random

def getArrayM(n):
    if n<=10:
        a = [7, 4, 9, 1, 6, 3, 5, 8, 2, 0]
    elif n<=20:
        a = [17, 7, 13, 4, 10, 9, 0, 12, 11, 1, 15, 6, 16, 3, 19, 5, 18, 8, 14, 2]
    elif n<=30:
        a = [13, 4, 27, 28, 25, 17, 10, 7, 20, 12, 24, 15, 19, 5, 18, 6, 16, 21, 11, 1, 0, 23, 3, 9, 8, 22, 14, 2, 26, 29]
    elif n<=60:
        a = [33, 51, 38, 13, 46, 59, 4, 52, 30, 27, 32, 43, 25, 47, 42, 36, 17, 41, 10, 49, 7, 20, 48, 12, 58, 24, 15, 50, 19, 5, 18, 40, 6, 37, 53, 16, 45, 21, 39, 11, 35, 54, 1, 0, 55, 23, 3, 9, 56, 8, 22, 44, 14, 57, 2, 26, 31, 28, 34, 29]
    else:
        a = getArrayRndM(0, n)
    return a


def getArrayRndM(lo, hi):
    int = random.random()


# http://www.careercup.com/question?id=5398298810646528
def randRepData(n):
    a = []
    for i in range(n):
        a += [i] * random.randint(0, n-1)
    random.shuffle(a)
    return a

def printArr(a, start, end):
    for i in range(start, end+1):
        print(a[i], end=", ")
    print()