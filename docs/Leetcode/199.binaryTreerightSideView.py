# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        if not root:
            return []
        levels = []
        while q:
            element_count = len(q)
            current_level = []
            for i in range(element_count):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                current_level.append(node.val)
            if len(current_level) > 0:
                levels.append(current_level)

        return [x[-1] for x in levels]
