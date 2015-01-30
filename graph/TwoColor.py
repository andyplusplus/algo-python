__author__ = 'andy'

class TwoColor:
    def __init__(self, g):
        self.marked = [False]*g.V()
        self.color = [False]*g.V()
        self.colorable = True
        for i in range(g.V()):
            if not self.marked[i]:
                self.dfs(g, i)

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.adj[v]:
            if self.colorable == False: return
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(g, w)
            elif self.color[w] == self.color[v]:
                self.colorable = False


