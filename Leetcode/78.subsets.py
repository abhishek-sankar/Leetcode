class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, subset):
            if start == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[start])
            backtrack(start + 1, subset)
            subset.pop()
            # while start + 1 < len(nums) and nums[start] == nums[start + 1]:
            #     start += 1
            #     continue
            backtrack(start + 1, subset)

        backtrack(0, [])
        return res
