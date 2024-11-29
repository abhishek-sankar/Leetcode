# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        start, end = head, prev

        while end.next:
            start.next, start = end, start.next
            end.next, end = start, end.next
        
        return head