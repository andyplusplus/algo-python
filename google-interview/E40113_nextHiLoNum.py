# Andy Wu
# Solutions to Google Interview Question


__author__ = 'andy'

'''
11100111010111:
next highest:
  find first increase:
               11100111010111
                          ^
       swap    11100111011011
   hi bit righ 11100111011110

next lowest:
  find first decrease:
               111001110101110
                         __i
       swap    111001110011110
  hi bit left
'''

def toggleBit2(n, offset):
    m = n^(1<<i)
    return m

def nextLow(n):
    testBit = lambda n, offset: (n & (1<<offset))>0
    toggleBit = lambda n, offset: n^(1<<offset)
    setbit = lambda n, offset: n & 1<<offset
    clearbit = lambda n, offset: n & ~(1<<offset)
    #1. find first decrease
    i = 0
    while n> (1<<(i+1)):
        if(testBit(n, i+1)>testBit(n, i)):
            n = toggleBit(n, i)
            n = toggleBit(n, i+1)
            break
        i+=1
    if n<=(1<<(i+1)): return None
    # hibit right: count hibits,
    # right bits: 1, leftBits:0
    hibits = 0
    for j in range(0, i+1):
        hibits += testBit(n, i)
    for j in range(i-hibits+1):
        clearbit(n, j)
    for j in range(i-hibits+1, i+1):
        setbit(n, j)
    return n

def nextHigh(n):
    a = list(bin(n))
    if a[2] == 'b': a = a[2:]
    N = len(a)
    #find first increase, swap
    i = N-1
    while i>3:
        if a[i-1]<a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            break
        i-=1

    if i==3: return n
    #move hi bit right:
    hiBits = 0
    for j in range(i, N):
        if a[j] == '1': hiBits += 1
    for j in range(N-1, N-1-hiBits, -1):
        a[j] = '1'
    for j in range(i, N-hiBits):
        a[j] = '0'
    str = "".join(a)
    n = int(str, 2)
    return n

def test():
    m = int("11100111010111", 2);
    print("Origina:", bin(m))
    n = nextHigh(m)
    #print("Next Hi:", bin(n))
    n = nextLow(m)
    print("Next Lo:", bin(n))
    print("Shld Lo: 0b11100111001111")

test()