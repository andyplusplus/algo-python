__author__ = 'andy'

from Graph import Graph

'''Count Connected Component'''
class CC:
    def __init__(self, g):
        self.count = 0
        self.id = [0]*g.V()
        visited = [0]*g.V()
        for i in range(g.V()):
            if not visited[i]:
                self.dfs(g, i, visited)
                self.count += 1

    def dfs(self, g, i, visited):
        visited[i] = True
        self.id[i] = self.count
        for i in g.adj[i]:
            if not visited[i]:
                self.dfs(g, i, visited)

    def connected(self, v, w):
        self.id[v] = self.id[w]

    def count(self):
        return self.count

    def id(self, v):
        return self.id[v]

def test():
    g = Graph.getGraph("tinyG.txt")
    cc = CC(g)
    print(cc.count)

if __name__ == '__main__': test()

