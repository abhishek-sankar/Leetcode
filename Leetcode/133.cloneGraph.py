"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        graph = {}
        queue = deque()
        queue.append(node)
        root = Node(node.val)
        graph[node.val] = root
        while(queue):
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in graph:
                    graph[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                graph[node.val].neighbors.append(graph[neighbor.val])
            
        return root