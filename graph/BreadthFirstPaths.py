__author__ = 'andy'

from Graph import Graph

class BreadthFirstPaths:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.pathTo = [-1]*graph.V()
        self.visited = [False]*graph.V()
        self.bfs(start)

    def bfs(self, v):
        queue=[v]
        self.visited[v] = True
        while len(queue):
            v = queue[0]; del queue[0]
            for w in self.graph.adj[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self.pathTo[w] = v
                    queue.append(w)

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
    paths = BreadthFirstPaths(g, 0)
    for i in range(1, g.V()):
        print(i, ":", paths.pathsTo(i))

if __name__ == '__main__': test()