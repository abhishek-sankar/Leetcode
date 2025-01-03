# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def has_cycle(head):
            visited = set()
            current = head

            while(current):
                if current in visited:
                    return current
                visited.add(current)
                current = current.next
            return None
        return has_cycle(head)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow
