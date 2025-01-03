class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = float("inf")
        while l <= r:
            while l <= r and l + 1 < len(nums) and nums[l] == nums[l + 1]:
                l += 1
            while l <= r and r > 0 and nums[r] == nums[r - 1]:
                r -= 1
            mid = (l + r) // 2
            lowest = min(lowest, nums[mid])
            if nums[l] <= nums[mid] < nums[r]:
                return nums[l]
            if nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid

        return lowest if lowest != float("inf") else -1
