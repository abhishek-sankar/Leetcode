# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # odd_head = ListNode(0)
        # even_head = ListNode(0)

        if head is None or head.next is None:
            return head

        odd_head = head
        even_head = head.next

        odd_runner = odd_head
        even_runner = even_head
        node = head
        node = node.next.next

        while node and odd_runner and even_runner:
            # print(node.val)
            odd_runner.next = node
            odd_runner = node
            node = node.next
            if node:
                # print(node.val)
                even_runner.next = node
                even_runner = node
                node = node.next
        odd_runner.next = even_head
        even_runner.next = None
        return odd_head
