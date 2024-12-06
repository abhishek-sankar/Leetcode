import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)

        while len(self.min_heap) > 0 and len(self.max_heap) > 0 and self.min_heap[0] < -1 * self.max_heap[0]:
            low = heapq.heappop(self.min_heap)
            high = heapq.heappop(self.max_heap)

            heapq.heappush(self.min_heap, -1 * high)
            heapq.heappush(self.max_heap, -1 * low)
        
        while len(self.min_heap) > len(self.max_heap) + 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * num)

        while len(self.max_heap) > len(self.min_heap) + 1:
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1 * num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            res = (self.min_heap[0] - self.max_heap[0]) / 2
            return res
        elif len(self.min_heap) > len(self.max_heap):
            res = self.min_heap[0]
            return res
        else: 
            res = -1 * self.max_heap[0]
            return res

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()