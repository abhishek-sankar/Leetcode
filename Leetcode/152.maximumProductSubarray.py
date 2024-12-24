class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1
        res = float("-inf")
        for num in nums:
            temp = min_prod * num
            min_prod = min(min_prod * num, num, max_prod * num)
            max_prod = max(max_prod * num, temp, num)
            res = max(res, max_prod)

        return res
