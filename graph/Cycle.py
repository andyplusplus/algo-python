__author__ = 'andy'

class cycle:
    def __init__(self, g):
        self.hasCycle = False
        self.marked = [False]*g.V()
        for i in range(g.V()):
            if not self.marked[i]:
                self.dfs(g, i, i)

    def dfs(self, g, v, u):
        self.marked[v] = True
        for w in g.adj[v]:
            if self.hasCycle: return
            if not self.marked[w]:
                self.dfs(g, w, v)
            elif (v!=w):
                self.hasCycle = True

    def hasCycle(self):
        return self.hasCycle

