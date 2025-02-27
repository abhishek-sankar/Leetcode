# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list1 else list2

        big, small = (list1, list2) if list1.val > list2.val else (list2, list1)
        while big is not None and small is not None:
            while small.next and small.next.val < big.val:
                small = small.next
            small.next, small = big, small.next
            small, big = big, small
        
        big, small = (list1, list2) if list1.val > list2.val else (list2, list1)
        return small