class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_sum = float("-inf")
        current_sum = 0
        heap = []
        pairs = sorted(zip(nums2, nums1), reverse=True)
        print(pairs)
        for mul, num in pairs:
            heapq.heappush(heap, num)
            current_sum += num

            if len(heap) > k:
                num = heapq.heappop(heap)
                current_sum -= num
            if len(heap) == k:
                print(heap, mul)
                max_sum = max(max_sum, current_sum * mul)

        return max_sum
