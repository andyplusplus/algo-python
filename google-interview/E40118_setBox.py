__author__ = 'andy'



def mainM():
    strs = 'abcde fghij klmno pqrst uvwxy z'.split()
    arr = [list(e) for e in strs]
    words = ['con', "zebrazfg", "loz"]
    for word in words:
        print("\n", word)
        pathM(arr, word)

def getPosM(c):
    seq = ord(c) - ord('a')
    r = seq//5
    c = seq%5
    return r,c

def getDesc_i_M(dir):
    if(dir>0):
        return " v "
    else:
        return " ^ "
def getDesc_j_M(dir):
    if(dir>0):
        return " > "
    else:
        return " < "
def moveY_M(j0, j1):
    incr = 1 if j0<j1 else -1
    for j in range(j0, j1, incr):
        print(getDesc_j_M(incr), end="")
def moveX_M(i0, i1):
    incr = 1 if i0<i1 else -1
    for i in range(i0, i1, incr):
        print(getDesc_i_M(incr), end="")


def pathM(a, word):
    M = len(a)
    N = len(a[0])
    print("from", 'a:', end=" ")
    i0,j0 = getPosM('a')
    iz,jz = getPosM('z')
    for c in word:
        i1,j1=getPosM(c)
        if [i0,j0] == [iz,jz]:#move __i first
            moveX_M(i0, i1)
            moveY_M(j0, j1)
        else:
            moveX_M(i0, i1)
            moveX_M(i0, i1)

        print("  to", c)
        i0,j0 = i1,j1

mainM()