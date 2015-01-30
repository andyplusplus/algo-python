__author__ = 'andy'

from Topological import Topological
from DiGraph import DiGraph
from DepthFirstOrder import DepthFirstOrder

class KosarajuSharirSCC:
    def __init__(self, g):
        self.id = [0] * g.V
        self.count = 0
        self.__marked = [False] * g.V
        order = DepthFirstOrder(g.reverse()).reversePost()
        print("Topological Order:", order)
        for v in order:
            if not self.__marked[v]:
                self.dfs(g, v)
                self.count += 1

    def dfs(self, g, v):
        self.id[v] = self.count
        self.__marked[v] = True
        for w in g.adj[v]:
            if not self.__marked[w]:
                self.dfs(g, w)

    def stronglyConnected(self, v, w):
        return self.id(w) == self.id(v)

    def count(self):
        return self.count

    def id(self, v):
        return self.id[v]

from unittest import TestCase
class Test_SCC(TestCase):
    def test(self):
        dg = DiGraph(fileName = "tinyDG.txt")
        scc = KosarajuSharirSCC(dg)
        print("scc count", scc.count)
        for i in range(scc.count):
            print(i, ": ",end="")
            for v in range(dg.V):
                if scc.id[v] == i:
                    print(v, end=" ")
            print("")
        self.assertTrue(scc.count==5)
