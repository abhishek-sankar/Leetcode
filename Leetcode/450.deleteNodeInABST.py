# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node
        # check children
        # 0 return None / delete node
        # 1 return left if left else right
        # 2 find min, copy to root and delete from right
        # always return root in recursion
        def deleteNode(root, val):
            if root is None:
                return None
            elif root.val < val:
                root.right = deleteNode(root.right, val)
            elif root.val > val:
                root.left = deleteNode(root.left, val)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    pred = findMax(root.left)
                    root.val = pred.val
                    root.left = deleteNode(root.left, pred.val)
            return root

        def findMax(root):
            while root.right:
                root = root.right
            return root

        return deleteNode(root, key)
