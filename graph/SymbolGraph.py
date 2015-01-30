__author__ = 'andy'

from util.In import In
from Graph import Graph

class SymbolGraph:
    def __init__(self, fileName, delim):
        inn=In(fileName)
        self.hashh = {}
        for i in range(len(inn.items)):
            if(not inn.items[i] in self.hashh):
                self.hashh[inn.items[i]] = len(self.hashh)
        self.arr = [""] * len(self.hashh)
        for keyy in self.hashh.keys():
            self.arr[self.hashh.get(keyy)] = keyy
        self.g = Graph(len(self.hashh))
        for i in range(0, len(inn.items), 2):
            v = self.hashh[inn.items[i]]
            w = self.hashh[inn.items[i+1]]
            self.g.addEdge(v, w)

    def contains(self, item):
        return item in self.hashh

    def __contains__(self, item):
        return item in self.hashh

    def index(self, key):
        return self.hashh[key]

    def name(self, v):
        return self.arr[v]

    def G(self):
        return self.g

def test():
    sg = SymbolGraph("routes.txt", " ")
    src = "JFK"
    idx = sg.index(src)
    print(src)
    for v in sg.g.adj[idx]:
        print(" ", sg.name(v))

if __name__ == '__main__':
    test()