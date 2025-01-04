class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1] if (mid + 1) < len(nums) else float("-inf"):
                r = mid
            else:
                l = mid + 1
        return l


# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if (nums[i] > nums[i - 1] if i > 0 else True) and (
#                 nums[i] > nums[i + 1] if i < len(nums) - 1 else True
#             ):
#                 return i
