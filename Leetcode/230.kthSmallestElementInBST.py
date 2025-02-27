# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root, res):
            if root is None:
                return
            res.append(root.val)
            inorder(root.left, res)
            inorder(root.right, res)
        inorder(root, res)
        res.sort()
        return res[k - 1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = deque()
        current = root
        count = 0
        while s or current:

            while(current):
                s.append(current)
                current = current.left
            current = s.pop()
            count +=1
            if count == k:
                return current.val

            current = current.right
        