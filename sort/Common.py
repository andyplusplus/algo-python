__author__ = 'andy'

import SortUtil

class Common:
    def __init__(self, a=None):
        if a==None:
            self.a = SortUtil.getArrayM(30)
        else:
            self.a = a

    def sort(self):
        pass

    def test(self):
        print("before", self.a)
        self.sort()
        print("after ", self.a)


from unittest import TestCase
class Test_Common(TestCase):
    def test(self):
        common = Common()
        common.test()