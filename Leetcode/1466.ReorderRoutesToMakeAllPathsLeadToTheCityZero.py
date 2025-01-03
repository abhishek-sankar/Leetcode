class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def buildGraph(edges):
            graph = {x: [] for x in range(n)}
            for edge in edges:
                a, b = edge
                graph[a].append(b)
                graph[b].append(a)
                edgeset.add((a, b))

            return graph

        visited = set()
        edgeset = set()
        graph = buildGraph(connections)
        reverse_count = [0]

        def dfs(i):
            visited.add(i)
            for neighbour in graph[i]:
                if neighbour not in visited:
                    if (i, neighbour) in edgeset:
                        reverse_count[0] += 1
                    dfs(neighbour)

        dfs(0)
        # print(edgeset)
        # print(graph)
        return reverse_count[0]
