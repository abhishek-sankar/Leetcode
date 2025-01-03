class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        total_sum = sum(nums)
        pivot = 0
        pivot_count = 0
        for pivot in range(len(nums) - 1):
            if 2 * prefix_sum[pivot] >= total_sum:
                pivot_count += 1

        return pivot_count
