class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        pivot = -1
        # check for 2 element arrs

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        if pivot == -1:
            nums[:] = sorted(nums)
            return
        next_min = float("inf")
        suffix = -1
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > nums[pivot]:
                suffix = j
                break
        # print(nums[pivot], nums[suffix])
        # print([num for num in reversed(nums[suffix+1:])])
        nums[pivot], nums[suffix] = nums[suffix], nums[pivot]
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])
