class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start >= 0 and nums[start] == nums[mid]:
                    start -= 1
                while end < len(nums) and nums[end] == nums[mid]:
                    end += 1
                start += 1
                end -= 1
                return [start, end]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]
