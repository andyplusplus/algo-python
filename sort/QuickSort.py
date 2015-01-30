__author__ = 'andy'

from Common import Common

class QuickSort(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        N = len(self.a)
        self.sortAux(0, len(self.a)-1)

    def sortAux(self, lo, hi):
        if lo>=hi: return
        pivot = self.partition(lo, hi)
        self.sortAux(lo, pivot-1)
        self.sortAux(pivot+1, hi)

    def partition(self, lo, hi):
        i=lo; j=hi; pivot=self.a[lo]
        while i<j:
            while i<j and pivot<self.a[j]: j -= 1
            self.a[i] = self.a[j]
            while i<j and self.a[i]<pivot: i += 1
            self.a[j] = self.a[i]
        self.a[i] = pivot
        return i


from unittest import TestCase
class Test_QuickSort(TestCase):
    def test(self):
        sel = QuickSort()
        sel.test()