class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = [x for x in candidates if x <= target]
        nums.sort()
        res = []

        def backtrack(start, used, current_sum):
            if current_sum == target:
                res.append(used.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if current_sum + nums[i] <= target:
                    used.append(nums[i])
                    backtrack(i + 1, used, current_sum + nums[i])
                    used.pop()

        backtrack(0, [], 0)
        return res
