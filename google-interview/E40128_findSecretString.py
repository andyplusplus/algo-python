__author__ = 'andy'

def combM(a, str, i):
    N = len(a)
    if(i==N):
        print("".join(a), end=" ")
        return
    a[i] = str[i].lower()
    combM(a, str, i+1)
    a[i] = str[i].upper()
    combM(a, str, i+1)

def combM2(str):
    testBit = lambda a, i: a & (1<<i)
    N = len(str)
    a = [""]*N
    str0 = str.lower()
    strz = str.upper()
    for i in range(2**N):
        #print(__i, end=" ")
        for j in range(N):
            if testBit(i, j): a[j] = strz[j]
            else: a[j] = str0[j]
        print("".join(a), end=" ")


def test():
    str = "abc"
    a = [0]*len(str)
    combM(a, str, 0)
    print()
    combM2(str)

test()