from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        pq = PriorityQueue()
        for num in counts:
            pq.put((-counts[num], num))
        
        res = []
        for i in range(k):
            _, num = pq.get()
            res.append(num)
        return res