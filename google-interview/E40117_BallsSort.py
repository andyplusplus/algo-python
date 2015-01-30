# Andy Wu
# Solutions to Google Interview Question


__author__ = 'andy'
'''
Not tested
'''
from sort.SortUtil import *

def sortM():
    a = randRepData(500) #generage around #125000 numbers
    print(a)
    #count
    count = [0]*500
    for i in range(len(a)):
        count[a[i]]+=1
    #calculate index of last elem
    count[0] -= 1
    #move
    for i in range(1, len(a)):
        count[i] += count[i-1]
    #output
    for i in range(len(a)-1, -1, -1):
        return

sortM()



