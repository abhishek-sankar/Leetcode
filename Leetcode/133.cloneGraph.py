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
    
'''
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
        q = deque()
        q.append(node)

        nodes = {}
        root = Node(node.val)
        nodes[node.val] = root

        while q:
            _next = q.popleft()
            for child in _next.neighbors:
                # print(child.val)
                if child.val not in nodes:
                    print(child.val)
                    q.append(child)
                    nodes[child.val] = Node(child.val)
                nodes[_next.val].neighbors.append(nodes[child.val])
        return root
'''