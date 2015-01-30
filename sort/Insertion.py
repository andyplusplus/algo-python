__author__ = 'andy'

from Common import Common

class Insertion(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        N = len(self.a)
        for i in range(1, N):
            tmp = self.a[i]
            while i>=1 and tmp < self.a[i-1]:
                self.a[i] = self.a[i-1]
                i -= 1
            self.a[i] = tmp

from unittest import TestCase
class Test_Insertion(TestCase):
    def test(self):
        sel = Insertion()
        sel.test()