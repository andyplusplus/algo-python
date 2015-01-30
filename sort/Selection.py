__author__ = 'andy'

from Common import Common

class Selection(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        N = len(self.a)
        for i in range(N):
            k=i
            for j in range(i+1, N):
                if self.a[j]<self.a[k]: k = j
            self.a[i], self.a[k] = self.a[k], self.a[i]

from unittest import TestCase
class Test_Selection(TestCase):
    def test(self):
        sel = Selection()
        sel.test()