__author__ = 'andy'

from Common import Common

class Shell(Common):
    def __init__(self, a=None):
        super().__init__(a)

    def sort(self):
        N = len(self.a)
        M = 1
        while 3*M<N:
            M = M*3+1
        while M>0:
            for i in range(M, N, M):
                tmp = self.a[i]
                while i>=M and tmp < self.a[i-M]:
                    self.a[i] = self.a[i-M]
                    i -= M
                self.a[i] = tmp
            M //= 3

from unittest import TestCase
class Test_Shell(TestCase):
    def test(self):
        sel = Shell()
        sel.test()