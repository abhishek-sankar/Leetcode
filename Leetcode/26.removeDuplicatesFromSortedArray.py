class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for start in range(1, len(nums)):
            if nums[start] == nums[start - 1]:
                continue
            else:
                nums[index] = nums[start]
                index += 1
        
        return index