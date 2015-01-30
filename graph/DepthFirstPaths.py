__author__ = 'andy'

from Graph import Graph

class DepthFirstPaths:

    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.pathTo = [-1]*graph.V()
        self.visited = [False]*graph.V()
        self.dfs(start)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.graph.adj[v]:
            if not self.visited[w]:
                self.pathTo[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathsTo(self, v):
        if not self.hasPathTo(v): return None
        pathList = []
        while v != self.start:
            pathList.insert(0, v)
            v = self.pathTo[v]
        pathList.insert(0, self.start)
        return pathList

def test():
    g = Graph.getGraph("tinyCG.txt")
    paths = DepthFirstPaths(g, 0)
    for i in range(1, g.V()):
        print(i, ":", paths.pathsTo(i))

if __name__ == '__main__': test()