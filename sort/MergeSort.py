__author__ = 'andy'

from Common import Common

# <editor-fold desc="class MergeSort">
class MergeSort(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        aux = [0]*len(self.a)
        self.sortAux(aux, 0, len(aux)-1)

    def sortAux(self, aux, lo, hi):
        if lo>=hi: return
        mid = (lo+hi)//2
        self.sortAux(aux, lo, mid)
        self.sortAux(aux, mid+1, hi)
        self.merge(aux, lo, mid, hi)

    def merge(self, aux, lo, mid, hi):
        if hi-lo<=0: return
        i = lo; j=mid+1
        for k in range(lo, hi+1):
            if i==mid+1: aux[k] = self.a[j]; j+=1
            elif j==hi+1: aux[k] = self.a[i]; i+=1
            elif self.a[i]<self.a[j]: aux[k] = self.a[i]; i+=1
            else: aux[k] = self.a[j]; j+=1
        for i in range(lo, hi+1): self.a[i] = aux[i]
# </editor-fold>

class MergeBU(MergeSort):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        aux = [0]*len(self.a)
        N = len(self.a); sz = 2
        while sz//2<N:
            i = 0
            while i<N:
                lo = i; mid=lo+sz//2-1; hi=min(N-1, lo+sz-1)
                self.merge(aux, lo, mid, hi)
                i+=sz
            sz *= 2

from unittest import TestCase
class Test_Merge(TestCase):
    def testMergeSort(self):
        sort = MergeSort()
        sort.test()

    def testMergeBU(self):
        sort = MergeBU()
        sort.test()