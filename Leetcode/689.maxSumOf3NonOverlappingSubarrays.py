class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [0] * (len(nums) - k + 1)
        sums[0] = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            sums[i] = sums[i - 1] + nums[k + i - 1] - nums[i - 1]

        left = [0] * (len(nums) - k + 1)
        right = [0] * (len(nums) - k + 1)

        current_max_left = 0
        for i in range(len(sums)):
            if sums[i] > sums[current_max_left]:
                current_max_left = i
            left[i] = current_max_left

        current_max_right = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[current_max_right]:
                current_max_right = i
            right[i] = current_max_right

        max_sum = float("-inf")
        indices = []
        for mid in range(k, len(sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            if sums[l] + sums[mid] + sums[r] > max_sum:
                max_sum = sums[l] + sums[mid] + sums[r]
                indices = [l, mid, r]
        return indices
