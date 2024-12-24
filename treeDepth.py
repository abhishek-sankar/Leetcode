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
        visited.add(start)
        for neighbour in self.graph_dict[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def findMaxDepthFromNode(self, node, depth, visited):
        if len(self.graph_dict[node]) == 0:
            return depth
        visited.add(node)
        depths = []
        for neighbour in self.graph_dict[node]:
            if neighbour not in visited:
                depths.append(self.findMaxDepthFromNode(neighbour, depth + 1, visited))

        return max(depths) if len(depths) > 0 else depth


graph = Graph([(0, 1), (0, 7), (7, 2), (1, 3), (1, 4), (2, 5), (2, 6)])
visited = set()
# graph.dfs(0, visited)
diameters = []
for node in graph.graph_dict:
    visited.clear()
    diameters.append((node, graph.findMaxDepthFromNode(node, 0, visited)))

min_diameter = min(diameters, key=lambda x: x[1])
min_nodes = [node for node in diameters if node[1] == min_diameter]
