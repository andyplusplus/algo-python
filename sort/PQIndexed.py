__author__ = 'andy'

from PQ import PQUtil
import SortUtil

# <editor-fold desc="IndexPQ">
class IndexPQ:#based on index MaxPQ
    def __init__(self, max, cmp=None):
        self.max = max
        self.pq = [-1]*self.max
        self.qp = [-1]*self.max
        self.keys = [0]*self.max
        self.n=0
        self.cmp = cmp
        if not cmp: self.cmp = PQUtil.PQMaxCmp
        self.dbgV = [0]*self.max #for debug purposes

    def isEmpty(self): return self.n == 0
    def contains(self, k): return self.qp[k] != -1

    def __cmpKeys(self, i, j):
        if self.__keyPQ(i) == self.__keyPQ(j):
            return 0
        elif self.cmp(self.__keyPQ(i), self.__keyPQ(j)):
            return -1
        else: #<
            return 1

    def __keyPQ(self, i):
        return self.keys[self.pq[i]]

    def __dbg(self): #for debug purposes
        for i in range(self.n):
            self.dbgV[i] = self.__keyPQ(i)
        print(self.dbgV)

    def __swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
        #self.__dbg()

    def swimUp(self, i):
        while i>0:
            parent = PQUtil.parent(i)
            if self.__cmpKeys(parent, i)>0:
                self.__swap(i, parent)
            i = parent

    def sinkDn(self, i):
        while PQUtil.leftChild(i)<self.n:
            minC = PQUtil.leftChild(i); rc=PQUtil.rightChild(i)
            if rc<self.n and self.__cmpKeys(rc, minC)<0:
                minC = rc
            if self.__cmpKeys(minC, i)<0:
                self.__swap(minC, i)
            i = minC

    def insert(self, k, key):
        self.keys[k] = key
        self.pq[self.n] = k
        self.qp[k] = self.n
        self.n +=1
        self.swimUp(k)
        self.sinkDn(k)

    #for minPQ
    def min(self):
        if self.n>0: return self.__keyPQ(0)
        else: return None

    def delMin(self):
        value = None
        if self.n>0:
            value = self.__keyPQ(0)
            self.__swap(0, self.n-1)
            self.n -= 1
            self.sinkDn(0)
        return value

    #for maxPQ
    def max(self): return self.min()
    def delMax(self): return self.delMin()
# </editor-fold>

class IndexMinPQ(IndexPQ):
    def __init__(self, max):
        super().__init__(max, PQUtil.PQMinCmp)

class IndexMaxPQ(IndexPQ):
    def __init__(self, max):
        super().__init__(max, PQUtil.PQMaxCmp)


from unittest import TestCase
class Test_PQIndex(TestCase):
    def test(self):
        a = SortUtil.getArrayM(60) #; print(list(range(0, len(a))))
        print(a)
        PQs = [IndexMinPQ, IndexMaxPQ]
        for PQ in PQs:
            pq = PQ(len(a))
            for i in range(len(a)):
                pq.insert(i, a[i])
                self.assertTrue(pq.contains(i))
                if i+1<len(a): self.assertTrue(not pq.contains(i+1))
            for i in range(len(a)):
                print(pq.delMin(), end=" ")
            print()