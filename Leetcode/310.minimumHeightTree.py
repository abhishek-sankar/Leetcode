from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        def createAdjacencyList(edges):
            adj = {}
            for i in range(n):
                adj[i] = []
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        adj = createAdjacencyList(edges)

        leaves = deque([i for i in range(n) if len(adj[i]) <= 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_leaves = len(leaves)
            remaining_nodes -= remaining_leaves

            for _ in range(remaining_leaves):
                leaf = leaves.popleft()
                if adj[leaf]:
                    neighbour = adj[leaf].pop()
                    adj[neighbour].remove(leaf)
                    # degree[neighbour] -= 1
                    if len(adj[neighbour]) == 1:
                        leaves.append(neighbour)

        return list(leaves)

        return [i for i, _ in enumerate(degree) if i > 0]
