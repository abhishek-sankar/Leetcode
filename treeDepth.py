class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            if end not in self.graph_dict:
                self.graph_dict[end] = []
            self.graph_dict[start] = [end]
            self.graph_dict[end] = [start]

    def dfs(self, start, visited):
        print(start.value)
        visited.add(start)
        for neighbour in self.graph_dict[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


graph = Graph([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])
graph.dfs(0, set())
