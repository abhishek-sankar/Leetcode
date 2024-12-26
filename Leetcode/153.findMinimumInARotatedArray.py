class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid

        return -1
