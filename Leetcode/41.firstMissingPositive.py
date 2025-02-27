class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains1 = False
        for num in nums:
            if num == 1:
                contains1 = True
                break
        if not contains1:
            return 1

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            value = abs(nums[i])
            if value == n:
                nums[0] = abs(nums[0]) * -1
            else:
                nums[value] = abs(nums[value]) * -1

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n

        return n + 1


"""
class Solution:
def firstMissingPositive(self, nums: List[int]) -> int:
	res = set([num for num in nums if num > 0])
	if len(res) == 0:
		return 1
	for i in range(1, max(res)):
		if i not in res:
			return i
	return len(res) + 1
"""
