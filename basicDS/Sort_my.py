__author__ = 'andy'

def exch(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def bubble_my(a):
    exchanges = True
    i = len(a) - 1
    while i>0 and exchanges:
        exchanges = False
        for j in range(i):
            if a[j] > a[j+1]:
                exchanges = True
                exch(a, j, j+1)
        i -= 1

def selection_my(a):
    N = len(a)
    for i in range(N):
        k = i
        for j in range(i+1, N):
            if(a[j]<a[k]):
                k = j
        exch(a, k, i)

def insertion_my(a):
    N = len(a)
    for i in range(1, N):
        v = a[i]
        j = i-1
        while j>=0 and v<=a[j]:
             a[j+1] = a[j]
             j -= 1
        a[j+1] = v

def shell_my(a):
    N = len(a)
    step = 1
    while(step<N//3):
        step = step*3 + 1
    #write
    while(step>0):
        for i in range(step, N, step):
            v = a[i]
            j = i - step
            while 0<=j and v<a[j]:
                a[j+step] = a[j]
                j -= step
            a[j+step] = v
        step = step // 3


def merge_my(a, aux=None, lo=None, hi=None):
    if aux == None:
        N = len(a)
        aux = [0] * N
        lo = 0
        hi = N - 1
    if lo>=hi:
        return

    m = (lo+hi)//2
    merge_my(a, aux, lo, m)
    merge_my(a, aux, m+1, hi)
    i = lo
    j = m+1
    for k in range(lo, hi+1):
        if(i>m):
            aux[k] = a[j]
            j += 1
        elif(j>hi):
            aux[k] = a[i]
            i+=1
        else:
            if(a[i]>a[j]):
                aux[k] = a[j]
                j += 1
            else:
                aux[k] = a[i]
                i += 1
    for k in range(lo, hi+1):
        a[k] = aux[k]

def quick_my(a):
    quickhelper_my(a, 0, len(a)-1)

def quickhelper_my(a, lo=None, hi=None):
    if(lo>hi):
        return
    piv = partition(a, lo, hi)
    quickhelper_my(a, lo, piv-1)
    quickhelper_my(a, piv+1, hi)

def partition(a, lo, hi):
    i = lo
    j = hi
    while i<j:
        while i<j and a[i]<=a[j]:
            j -= 1
        exch(a, j, i)
        while i<j and a[i]<=a[j]:
            i += 1
        exch(a, i, j)
    return i

a = [33, 51, 38, 13, 46, 59, 4, 52, 30, 27, 32, 43, 25, 47, 42, 36, 17, 41, 10, 49, 7, 20, 48, 12, 58, 24, 15, 50, 19, 5, 18, 40, 6, 37, 53, 16, 45, 21, 39, 11, 35, 54, 1, 0, 55, 23, 3, 9, 56, 8, 22, 44, 14, 57, 2, 26, 31, 28, 34, 29]
#quick_my(a)
#print(a)
#bubble_my(a)
#selection_my(a)
#insertion_my(a)
#shell_my(a)
#merge_my(a)
print(a)
