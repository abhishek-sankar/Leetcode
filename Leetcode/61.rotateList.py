# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        start = ListNode(0)
        start.next = head
        count = 0
        while start and start.next:  # 1 - 2 - 3 - None
            count += 1
            start = start.next

        start.next = head

        k = k % count

        count = count - k

        start = ListNode(0)
        start.next = head
        while start and start.next and count:
            count -= 1
            start = start.next

        # start is the end for now
        dummy = ListNode(0)
        dummy.next = start.next

        start.next = None
        return dummy.next
