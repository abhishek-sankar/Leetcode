# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        f, s = headA, headB
        while f and s:
            if f == s:
                return f
            f = f.next
            s = s.next

        while f != s:
            f = f.next if f else headB
            s = s.next if s else headA

        return f
