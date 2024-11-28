# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def findMaxChildrenSum(root, res):
            if root is None:
                return 0
            left = findMaxChildrenSum(root.left, res)
            right = findMaxChildrenSum(root.right, res)
            res[0] = max(res[0], root.val, root.val + left, root.val + right, root.val + left + right)
            _max = root.val + max(left, right, 0)
            
            return _max

        _max = findMaxChildrenSum(root, res)
        return max(_max, res[0])
        