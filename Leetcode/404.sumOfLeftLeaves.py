# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def sumLeft(root, pos):
            if root is None:
                return 0
            if not root.left and not root.right and pos == "l":
                return root.val
            return sumLeft(root.left, "l") + sumLeft(root.right, "r")

        return sumLeft(root, "r")
