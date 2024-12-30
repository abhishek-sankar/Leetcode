# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        if not root:
            return 0
        levels = []
        while q:
            count = len(q)
            current_level = []
            for i in range(count):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                current_level.append(node.val)
            if len(current_level) > 0:
                levels.append(current_level)
        print(levels)
        return max(enumerate([sum(x) for x in levels]), key=lambda x: x[1])[0] + 1
