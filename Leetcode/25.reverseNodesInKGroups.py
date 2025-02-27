# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        def reverseList(
            head: Optional[ListNode],
        ) -> (Optional[ListNode], Optional[ListNode]):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return (prev, head)

        while True:
            count = 0
            start = prev.next
            end = prev
            for i in range(k):
                end = end.next
                if end is None:
                    return dummy.next

            next_group_head = end.next
            end.next = None

            reversed_head, reversed_tail = reverseList(start)
            prev.next = reversed_head
            reversed_tail.next = next_group_head
            prev = reversed_tail

        return dummy.next
