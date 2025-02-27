class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        dp_0 = [0] * (len(nums) - 1)
        dp_1 = [0] * (len(nums) - 1)
        dp_0[0] = nums[0]
        dp_0[1] = nums[1]
        dp_0[2] = max(nums[1], nums[0] + nums[2])

        dp_1[0] = nums[1]
        dp_1[1] = nums[2]
        dp_1[2] = max(nums[2], nums[1] + nums[3])

        for i in range(3, len(nums) - 1):
            dp_0[i] = max(dp_0[i - 2], dp_0[i-3]) + nums[i]
            dp_1[i] = max(dp_1[i - 2], dp_1[i - 3]) + nums[i + 1]
        
        # print(dp_0)
        # print(dp_1)
        return max(max(dp_0), max(dp_1))