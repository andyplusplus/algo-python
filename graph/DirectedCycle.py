__author__ = 'andy'

from DiGraph import DiGraph

class DirectedCycle:
    def __init__(self, g):
        self.marked = [False]*g.V
        self.cycle = None
        self.__g = g
        self.__inStack = [False]*g.V
        self.__pathTo = [0]*g.V

        for v in range(g.V):
            if self.cycle: return
            if not self.marked[v]:
                self.__pathTo[v] = v
                self.__dfs(v)

    def __dfs(self, v):
        self.__inStack[v] = True
        self.marked[v] = True
        for w in self.__g.adj[v]:
            if self.cycle: return
            if not self.marked[w]:
                self.__pathTo[w] = v
                self.__dfs(w)
            elif self.__inStack[w]:
                self.cycle = [w]
                while v != w:
                    self.cycle.insert(0, v)
                    v = self.__pathTo[v]
                self.cycle.insert(0, w)
                break
        self.__inStack[v] = False


    def hasCycle(self):
        return self.cycle != None

from unittest import TestCase
class TestDirectedCycle(TestCase):
    def test(self):
        g = DiGraph(fileName="tinyDG.txt")
        dc = DirectedCycle(g)
        print(dc.cycle)
        self.assertTrue(dc.cycle)
