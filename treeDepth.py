class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            if end not in self.graph_dict:
                self.graph_dict[end] = []
            self.graph_dict[start].append(end)
            self.graph_dict[end].append(start)

    def dfs(self, start, visited):
        print(start)
        visited.add(start)
        for neighbour in self.graph_dict[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def findMaxDepthFromNode(self, node, depth, visited):
        if len(adj[node]) == 0:
            return depth


graph = Graph([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])
visited = set()
graph.dfs(0, visited)
