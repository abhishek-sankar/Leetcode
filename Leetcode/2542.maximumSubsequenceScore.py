class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_sum = float("-inf")
        current_sum = 0
        heap = []
        pairs = sorted(zip(nums2, nums1), reverse=True)

        for i in range(k):
            mul, num = pairs[i]
            current_sum += num
            heapq.heappush(heap, num)

        max_sum = max(max_sum, current_sum * pairs[k - 1][0])
        for i in range(k, len(pairs)):
            num = heapq.heappop(heap)
            heapq.heappush(heap, pairs[i][1])
            current_sum = current_sum - num + pairs[i][1]
            max_sum = max(max_sum, current_sum * pairs[i][0])

        return max_sum


# class Solution:
#     def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         max_sum = float("-inf")
#         current_sum = 0
#         heap = []
#         pairs = sorted(zip(nums2, nums1), reverse=True)
#         print(pairs)
#         for mul, num in pairs:
#             heapq.heappush(heap, num)
#             current_sum += num

#             if len(heap) > k:
#                 num = heapq.heappop(heap)
#                 current_sum -= num
#             if len(heap) == k:
#                 print(heap, mul)
#                 max_sum = max(max_sum, current_sum * mul)

#         return max_sum
