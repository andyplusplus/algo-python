__author__ = 'andy'

from DiGraph import DiGraph

class DepthFirstOrder:
    def __init__(self, g):
        self.__preQ = []
        self.__postQ = []
        self.__reversePostS = []
        self.__marked = [False]*g.V
        for v in range(g.V):
            if not self.__marked[v]:
                self.__dfs(g, v)

    def __dfs(self, g, v):
        self.__marked[v] = True
        self.__preQ.append(v)
        for w in g.adj[v]:
            if not self.__marked[w]:
                self.__dfs(g, w)
        self.__postQ.append(v)
        self.__reversePostS.insert(0, v)

    def pre(self): return self.__preQ
    def post(self): return self.__postQ
    def reversePost(self):
        return self.__reversePostS

from unittest import TestCase
class TestDepthFirstOrder(TestCase):
    def test(self):
        g = DiGraph(fileName="tinyG.txt")
        gOrd = DepthFirstOrder(g)
        print(gOrd.pre())
        print(gOrd.post())
        print(gOrd.reversePost())
        #self.fail()