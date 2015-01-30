__author__ = 'andy'

from Common import Common

class Quick3way(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        self.sortAux(0, len(self.a)-1)

    #   k   i   j
    #000vvvvvzzzz
    def sortAux(self, lo, hi):
        if lo>=hi: return
        k=lo; i=lo; j=hi; p=self.a[lo]
        while i<=j:
            if self.a[i]==p: i+=1
            elif self.a[i]<p:
                self.a[i], self.a[k] = self.a[k], self.a[i]
                i+=1; k+=1
            else:#>0
                self.a[i], self.a[j] = self.a[j], self.a[i]
                j-=1
        self.sortAux(lo, k-1)
        self.sortAux(i, hi)

from unittest import TestCase
class Test_Quick3way(TestCase):
    def test(self):
        sorter = Quick3way()
        sorter.test()