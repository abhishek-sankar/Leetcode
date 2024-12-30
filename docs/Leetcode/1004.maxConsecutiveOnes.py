class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        l, r = 0, 0
        longest = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
