class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_avg = sum(nums[:k])
        avg = running_avg
        for i in range(k, len(nums)):
            running_avg += nums[i] - nums[i - k]
            avg = max(avg, running_avg)

        return avg / k
