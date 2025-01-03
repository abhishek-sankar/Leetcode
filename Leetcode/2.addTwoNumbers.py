# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l3 = ListNode(0)
        carry = 0
        while l1 and l2:
            l3.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                l3_next = ListNode(0)
                l3.next = l3_next
                l3 = l3.next

        if l1 or l2:
            l3_next = ListNode(0)
            l3.next = l3_next
            l3 = l3.next

        while l1:
            l3.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1 = l1.next
            if l1:
                l3_next = ListNode(0)
                l3.next = l3_next
                l3 = l3.next

        while l2:
            l3.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2 = l2.next
            if l2:
                l3_next = ListNode(0)
                l3.next = l3_next
                l3 = l3.next

        if carry:
            l3_next = ListNode(carry)
            l3.next = l3_next
            l3 = l3.next

        return head
