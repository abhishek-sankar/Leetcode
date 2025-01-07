# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse half the list
        # start from both ends
        # take max sum vals
        # return max
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow

        # slow.next = slow.next if fast and not fast.next else None

        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        start, end = head, prev
        max_twin_sum = float("-inf")
        while start and end and start != end:
            max_twin_sum = max(start.val + end.val, max_twin_sum)
            start = start.next
            end = end.next

        return max_twin_sum
