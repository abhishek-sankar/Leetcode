
 '''
 class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = set([num for num in nums if num > 0])
        if len(res) == 0:
            return 1
        for i in range(1, max(res)):
            if i not in res:
                return i
        return len(res) + 1
 '''