class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums) - nums[0]
        if l_sum == r_sum:
            return 0
        for i in range(1, len(nums)):
            l_sum += nums[i - 1]
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i

        return -1
