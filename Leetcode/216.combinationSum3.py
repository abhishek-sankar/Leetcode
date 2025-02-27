class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [x for x in range(9, 0, -1)]
        res = []

        def backtrack(index, current):
            if sum(current) == n and len(current) == k:
                res.append(current[:])
                return
            if len(current) > k or sum(current) > n or index > 8:
                return
            for i in range(index, 9):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return res
