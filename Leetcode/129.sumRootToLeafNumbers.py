# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumRootToLeaf(root, total):
            if root is None:
                return 0
            if not root.left and not root.right:
                return total * 10 + root.val
            if not root.left:
                return sumRootToLeaf(root.right, total * 10 + root.val)
            if not root.right:
                return sumRootToLeaf(root.left, total * 10 + root.val)

            return sumRootToLeaf(root.left, total * 10 + root.val) + sumRootToLeaf(
                root.right, total * 10 + root.val
            )

        return sumRootToLeaf(root, 0)
