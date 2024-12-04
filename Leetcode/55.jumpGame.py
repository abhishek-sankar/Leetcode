class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(len(nums)):
            if dp[i]:
                for j in range(i, min(i + nums[i] + 1, len(nums))):
                    dp[j] = 1
        return True if dp[len(nums) - 1] else False
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0: 
            return True
        gas = nums[0]
        for n in nums:
            if gas < 0:
                return False
            gas = max(gas, n)
            gas -=1
        return True
'''