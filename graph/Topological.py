__author__ = 'andy'

from DirectedCycle import DirectedCycle
from DepthFirstOrder import DepthFirstOrder
from SymbolDiGraph import SymbolDiGraph

class Topological:
    def __init__(self, g):
        self.isDAG = True
        self.order = None
        dc = DirectedCycle(g)
        if dc.hasCycle():
            self.isDAG = False
            print(dc.cycle)
        if self.isDAG:
            self.order = DepthFirstOrder(g).reversePost()

from unittest import TestCase
class TestTopological(TestCase):
    def test(self):
        sdg = SymbolDiGraph("jobs.txt","/")
        top = Topological(sdg.G)
        for v in top.order:
            print(sdg.strList[v], "-->", end="")


