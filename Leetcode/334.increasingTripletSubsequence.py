class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        last = nums[-1]
        second_last = None
        for i in range(len(nums) - 1, -1, -1):

            if second_last is None and nums[i] < last:
                second_last = nums[i]
                continue

            if nums[i] > last:
                last = nums[i]

            if nums[i] < last:
                if nums[i] < second_last:
                    return True
                second_last = nums[i]

        return False
