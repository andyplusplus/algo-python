# Andy Wu
# Solutions to Google Interview Question


__author__ = 'andy'


def getMedium_M(a):
    minV = min(a)
    maxV = max(a)
    N = maxV - minv + 1
    counter = [0]*N
    for i in a:
        counter[i-minV] += 1
    sum = 0
    for i, n in enumerate(a):
        sum += n
        if sum > N//2:
            return n