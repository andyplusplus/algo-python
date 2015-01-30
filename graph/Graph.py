__author__ = 'andy'
from util.In import In

class Graph:
    def __init__(self, v=0, fileName=None):
        self.e = 0
        self.adj = []
        if fileName:
            fileReader = In(fileName)
            self.v = fileReader.readint()
            for i in range(self.v): self.adj.append(set())
            e = fileReader.readint()
            for i in range(e):
                v0 = fileReader.readint()
                w0 = fileReader.readint()
                self.addEdge(v0, w0)
        else:
            self.v = v
            for i in range(self.v): self.adj.append(set())
        v = v

    def V(self): return self.v

    def E(self): return self.e

    def addEdge(self, v, w): #void
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.e +=1

    def adj(self, v): return self.adj

    def __str__(self):
        return ""

    @classmethod
    def getGraph(cls, fileName):
        g = Graph(0, fileName)
        return g