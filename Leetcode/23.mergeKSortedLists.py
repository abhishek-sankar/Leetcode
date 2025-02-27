from queue import PriorityQueue
from itertools import count
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        counter = count()
        for head in lists:
            if head is not None:
                pq.put((head.val, next(counter), head))
        
        dummy = ListNode()
        current = dummy
        while not pq.empty():
            val, index, old_head = pq.get()
            current.next = old_head
            current = old_head
            new_head = old_head.next
            if new_head is not None:
                pq.put((new_head.val, next(counter), new_head))
        
        return dummy.next