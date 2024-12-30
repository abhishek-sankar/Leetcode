class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        delete = 0
        max_len = 0
        for r in range(len(nums)):

            if nums[r] != 1:
                delete += 1

            while delete > 1:
                if nums[l] != 1:
                    delete -= 1
                l += 1

            max_len = max(max_len, r - l)

        return max_len
