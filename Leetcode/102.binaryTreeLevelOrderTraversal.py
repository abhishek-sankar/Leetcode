# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        q.append(root)
        while q:
            current = len(q)
            level = []
            for _ in range(current):
                node = q.popleft()
                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if len(level):
                res.append(level)
        
        return res
