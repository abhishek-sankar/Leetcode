# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        l, r = left, right
        l -= 1
        r -= l
        start = ListNode(0)
        start.next = head
        before = None
        after = None
        first = None
        end = None
        while l and start and start.next:
            l -= 1
            start = start.next
        before = start
        prev = None
        start = start.next
        first = start
        while r - 1 and start and start.next:
            r -= 1
            start.next, start, prev = prev, start.next, start

        end = start
        after = start.next
        end.next = prev

        before.next = end
        first.next = after

        return end if left == 1 else head
