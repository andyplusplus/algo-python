__author__ = 'andy'

class UF:
    def __init__(self, N):
        self.id = [i for i in range(N)]
        self.count = N

    #O(n)
    def union(self, p, q):
        pu = self.find(p)
        qu = self.find(q)
        if pu==qu: return
        lenn = len(self.id)
        for i in range(lenn):
            if self.id[i] == pu: self.id[i] = qu
        self.count -= 1

    #O(1)
    def find(self, p):
        while p!= self.id[p]:  #this will only run once in this case
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class QuickUF(UF):
    def __init__(self, N):
        super().__init__(N)

    def find(self, p): #will sun many times
        p = super().find(p)
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i==j: return
        self.id[i] = j
        self.count -= 1

class WeightedQuickUF(UF):
    def __init__(self, N):
        super().__init__(N)
        self.sz=[1]*N

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i==j: return
        if self.sz[i]>self.sz[j]: #j merge to i
            self.id[j]=i
            self.sz[i]+=self.sz[j]
        else: #i merge to j
            self.id[i] = j
            self.sz[j] += self.sz[i]
        self.count -= 1

from unittest import TestCase
from util.In import In

class Test_UF1(TestCase):
    def test(self):
        inn = In("tinyUF.txt")
        N = inn.readint()
        ufs = [UF(N), QuickUF(N), WeightedQuickUF(N)]
        for uf in ufs:
            inn.reset(); inn.readint()
            for i in range(1, len(inn.items), 2):
                p = inn.readint()
                q=inn.readint()
                uf.union(p, q)
            print(uf.count, end=" ")
            print(uf.connected(2, 1))