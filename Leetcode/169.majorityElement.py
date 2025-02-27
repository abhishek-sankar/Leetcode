class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = 0
        count = 1
        for i in range(len(nums)):
            if nums[i] == nums[maj]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj = i
                count = 1
        new_count = 0
        for i in range(len(nums)):
            if nums[i] == nums[maj]:
                new_count += 1
        
        return nums[maj] if new_count > len(nums) // 2 else -1