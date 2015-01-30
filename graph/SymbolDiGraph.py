__author__ = 'andy'

from util.In import In
from DiGraph import DiGraph
class SymbolDiGraph:
    def __init__(self, fileName, delimer=" "):
        self.str2Idx = {}
        self.strList = []
        inn = In(fileName, delimer)
        for item in inn.items:
            if item not in self.str2Idx:
                self.str2Idx[item] = len(self.str2Idx)
                self.strList.append(item)
        self.G = DiGraph(len(self.str2Idx))
        #add E
        for line in inn.lines:
            a = line.split(delimer)
            if(len(a)<=0): continue
            for i in range(1, len(a)):
                self.G.addEdge(self.str2Idx[a[0]], self.str2Idx[a[i]])

    def contains(self, str):
        return str in self.str2Idx

    def index(self, str):
        return self.str2Idx[str]


from unittest import TestCase
class Test_SymbolDiGraph(TestCase):
    def test(self):
        sd = SymbolDiGraph("jobs.txt", "/")
        str = "Machine Learning"
        self.assertTrue(sd.contains(str))
        print(sd.index(str))
