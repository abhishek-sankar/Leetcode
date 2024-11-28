class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = 0
        LIS = [0] * (len(nums))
        if len(nums) < 2:
            return len(nums)
        
        LIS[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                else:
                    LIS[i] = max(1, LIS[i])
        return max(LIS)


