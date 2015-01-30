__author__ = 'andy'

from DirectedDFS import DirectedDFS
from DiGraph import DiGraph

class TransitiveClosure:
    def __init__(self, dg):
        self.all= [DirectedDFS(dg, i) for i in range(dg.V)]

    def reachable(self, v, w):
        return self.all[v].marked[w]

from unittest import TestCase
class Test_TransitiveCloure(TestCase):
    def test(self):
        dg = DiGraph(fileName = "tinyDG.txt")
        tc = TransitiveClosure(dg)
        for w in range(1, dg.V):
            print(tc.reachable(0, w))