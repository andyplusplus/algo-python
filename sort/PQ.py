__author__ = 'andy'

class PQUtil:
    @classmethod
    def PQMaxCmp(cls, a, b): return a>b

    @classmethod
    def PQMinCmp(cls, a, b): return a<b

    @classmethod
    def leftChild(cls, i): return 2*i+1

    @classmethod
    def rightChild(cls, i): return 2*i+2

    @classmethod
    def parent(cls, c): return (c-1)//2




class PriorityQueue:
    def __init__(self, max=0, a=None, comparator=None):
        self.a = [0]*max
        self.max = max
        self.size = 0
        self.cmp = comparator if comparator else PQUtil.PQMaxCmp
        if a:
            self.a = a
            self.max = len(self.a)
            self.size = len(self.a)
        for i in range(self.size):
            self.swimup(i)

    def insert(self, v):
        if self.size<self.max:
            self.a[self.size] = v
            self.size += 1
        self.swimup(self.size-1)

    def delMax(self):
        if self.size>0:
            value = self.a[0]
            self.a[0] = self.a[self.size-1]
            self.size -= 1
            self.sinkDown(0)
            return value
        else: return None

    def swimup(self, i):
        while i>0:
            par = PQUtil.parent(i)
            if self.cmp(self.a[i], self.a[par]):
                self.a[i], self.a[par] = self.a[par], self.a[i]
            i = par

    #for node i, left: (i+1)*2-1, right: (i+1)*2
    def sinkDown(self, i):
        while PQUtil.leftChild(i)<self.size:
            leCh = PQUtil.leftChild(i); riCh = PQUtil.rightChild(i)
            maxCh = leCh
            if riCh<self.size and self.cmp(self.a[riCh], self.a[leCh]):
                maxCh = riCh
            if self.cmp(self.a[maxCh], self.a[i]):
                self.a[i], self.a[maxCh] = self.a[maxCh], self.a[i]
            else: break
            i = maxCh

    def max(self): return self.max
    def isEmpty(self): return self.size>0
    def size(self): return self.size

class MaxPQ(PriorityQueue):
    def __init__(self, max=0, a=None):
        super().__init__(max, a, PQUtil.PQMaxCmp)

class MinPQ(PriorityQueue):
    def __init__(self, max=0, a=None):
        super().__init__(max, a, PQUtil.PQMinCmp)

from unittest import TestCase
import SortUtil
class Test_MaxPQ(TestCase):
    def testPriorityQueue(self):
        cmps = [PQUtil.PQMaxCmp, PQUtil.PQMaxCmp, None]
        N = 60
        print(SortUtil.getArrayM(N))
        for cmp in cmps:
            pq = PriorityQueue(a=SortUtil.getArrayM(N), comparator= cmp)
            result = []
            print(cmp)
            for i in range(N):
                result.append(pq.delMax())
            print(result)

    def testPQ(self):
        PQs = [MinPQ, MaxPQ]
        print(SortUtil.getArrayM(N))
        for PQ in PQs:
            pq = PQ(a=SortUtil.getArrayM(N))
            result = []
            print(PQ)
            for i in range(N):
                result.append(pq.delMax())
            print(result)