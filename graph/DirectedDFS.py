__author__ = 'andy'

from DiGraph import DiGraph

# <editor-fold desc="class DirectedDFS">
class DirectedDFS:
    def __init__(self, g, s=0, sources=None):
        self.marked = [False]*g.V
        self.g = g
        if sources:
            for i in sources:
                if not self.marked[i]:
                    self.dfs(i)
        else:
            self.dfs(s)

    def dfs(self, s):
        self.marked[s] = True
        for v in self.g.adj[s]:
            if not self.marked[v]:
                self.dfs(v)

    def marked(self, v):
        return self.marked[v]
# </editor-fold> #class DirectedDFS


from unittest import TestCase
class TestDirectedDFS(TestCase):
    def test_DirectedDFS(self):
        g = DiGraph(0, "tinyDG.txt")
        dfs0 = DirectedDFS(g, 1)
        self.assertTrue(dfs0.marked[1])
        self.assertTrue(not dfs0.marked[0])