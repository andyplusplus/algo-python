__author__ = 'andy'

from functools import total_ordering

@total_ordering
class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, v):
        if(self.v == v): return self.w
        else: return self.v

    def __eq__(self, other):
        return self.weight == self.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return "v=%d, w=%d, wt=%.2f" % (self.v, self.w, self.weight)

# <editor-fold desc="class Edges -- comment off">
'''
class Edges(list):
    def __init__(self):
        super().__init__()

    def append(self, p_object):
        super().append(p_object)

    def __str__(self):
        str = ""
        for edge in self.__iter__():
            str += " || " + edge
        return str
'''
# </editor-fold>

from util.In import In
class EdgeWeightedGraph:
    def __init__(self, v=0, fileName=None):
        self.V = v
        if fileName:
            inn = In(fileName)
            self.V = int(inn.lines[0])
            self.E=0
            self.adj = [[] for i in range(self.V)]
            #parse the file, refer to tinyEWG.txt
            for i in range(2, len(inn.lines)):
                a = inn.lines[i].split()
                edge = Edge(int(a[0]), int(a[1]), float(a[2]))
                self.addEdge(edge)
        else:
            self.adj = [[] for i in range(self.V)]

    def addEdge(self, edge):
        self.adj[edge.v].append(edge)
        self.adj[edge.w].append(edge)
        self.E +=1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                if v<e.other(v):
                    edges.append(e)
        return edges

    def __str__(self):
        return "V=%d E=%d" % (self.V, self.E)


from unittest import TestCase
class TestEdgeWeightedGraph(TestCase):
    def testEdge(self):
        edge = Edge(1,2,3.4)
        print(edge)

    def testgraph(self):
        graph = EdgeWeightedGraph(fileName="tinyEWG.txt")
        print(graph.edges())
        print(graph)