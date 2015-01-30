# Andy Wu
# Solutions to Google Interview Question



__author__ = 'andy'

def findExch(a, mid, dif):
    a[:mid] = sorted(a[:mid])
    a[mid:] = sorted(a[mid:])


def div(a, mid, expS):
    sumR = sum(a, mid)
    while(True):
        dif = expS - sumR    #findElements: with left - right = dif
        if dif==0:
            print(mid-1, sumR, a)
        else:
            lst = findExch(a, mid, dif)
            for i,j in lst:
                a[i], a[j] = a[j], a[i]

def div_shift(a):
    expS = sum(a)//2
    mid = len(a)//2+1
    sumR = sum(a, mid, expS)
    return

# region brute force
def div_bf(a):
    sLe = sum(a)//2#    sRi = sum(a)-sLe
    aLe = [0]*(len(a)//2)
    aLe[0] = a[0]; a = a[1:len(a)]
    nLe = 1
    foundList = [None]
    div_bf_helper(a, aLe, nLe, sLe, foundList)

def div_bf_helper(a, aLe, nLe, sLe, foundList):
    if foundList[0]: return
    if nLe==len(a):
        if sum(aLe)==sLe:
            foundList[0] = aLe
            print(nLe, sum(a), a)
        return
    for i in range(len(a)):
        aLe[nLe] = a[i]
        b = a[:]; del b[i]
        div_bf_helper(b, aLe, nLe+1, sLe, foundList)
    return
# endregion

def test():
    a = [33, 51, 38, 13, 46, 59, 4, 52, 30, 27, 32, 43, 25, 47, 42, 36, 17, 41, 10, 49, 7, 8]
    #a = [1,2,16,26, 88, 99]
    print(len(a), sum(a), a)
    print("brute force: ")
    div_bf(a)
    print("dvide shift: ")
    div_shift(a)
    print(len(a), sum(a), a)

test()
