class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [x for x in range(1, 1001)]
        self.removed_elements = set()

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            removed = heapq.heappop(self.heap)
            self.removed_elements.add(removed)
            return removed

    def addBack(self, num: int) -> None:
        if num in self.removed_elements:
            heapq.heappush(self.heap, (num))
            self.removed_elements.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
