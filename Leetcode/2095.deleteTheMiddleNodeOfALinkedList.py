# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        prev = ListNode(0)
        prev.next = slow
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast.next and not fast.next.next:
            # even - delete slow
            if slow and slow.next and slow.next.next:  # check head
                slow.next = slow.next.next
        else:
            # odd - delete prev
            if prev and prev.next and prev.next.next:  # check head
                prev.next = prev.next.next
        if prev.next == head:
            if head.next is None:
                return None
            head.next = None

        return head
