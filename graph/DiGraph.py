__author__ = 'andy'

from util.In import In

# <editor-fold desc="class DiGraph">
class DiGraph:
    def __init__(self, v=0, fileName=None, delim=" "):
        self.E = 0
        if fileName:
            inn=In(fileName)
            self.V = inn.readint()
            self.adj = self.__getAdj__(self.V)
            E = inn.readint()
            for i in range(E):
                self.addEdge(inn.readint(), inn.readint())
        else:
            self.V = v
            self.adj = self.__getAdj__(self.V)

    def __getAdj__(self, v):
        adj = []
        for i in range(self.V):
            adj.append(set())
        return adj

    def addEdge(self, v, w):
        self.E += 1
        self.adj[v].add(w)

    def V(self): return self.V
    def E(self): return self.E

    def adj(self, v): return self.adj

    def reverse(self):
        g = DiGraph(self.V)
        for i in range(self.V):
            for j in range(len(self.adj[i])):
                g.addEdge(j, i)
        return g

    def __str__(self):
        return ""
# </editor-fold>  class DiGraph


from unittest import TestCase
class TestDiGraph(TestCase):
    def test_DiGraph(self):
        g = DiGraph(0, "tinyDG.txt")
        self.assertEqual(g.V, 13)
        self.assertEqual(g.E, 22)
        gr = g.reverse()
        self.assertEqual(gr.V, 13)
        self.assertEqual(gr.E, 22)