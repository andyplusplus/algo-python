__author__ = 'andy'

from PQ import MaxPQ
from Common import Common

class HeapSort(Common, MaxPQ):
    def __init__(self, arr=None):
        Common.__init__(self, arr)
        MaxPQ.__init__(self, a=self.a)

    def sort(self):
        savedSize = self.size
        for i in range(self.max-1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.size -= 1
            self.sinkDown(0)

from unittest import TestCase
class Test_(TestCase):
    def test(self):
        sorter = HeapSort()
        sorter.test()