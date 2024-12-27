class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(total, index):
            if index == len(nums):
                return 1 if total == target else 0

            if (total, index) in memo:
                return memo[(total, index)]

            add = backtrack(total + nums[index], index + 1)
            sub = backtrack(total - nums[index], index + 1)
            memo[(total, index)] = add + sub

            return memo[(total, index)]

        res = backtrack(0, 0)
        return res
