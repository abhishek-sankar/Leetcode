# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        rows = []
        q = deque()
        q.append(root)
        count = len(q)
        while q:
            current_row = []
            count = len(q)
            for i in range(count):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    current_row.append(node.val)
            if len(current_row):
                rows.append(current_row)
        # print(rows)
        return [max(row) for row in rows]

        