class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float("inf")
        closest_total = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return target
                elif total > target:
                    r -= 1
                elif total < target:
                    l += 1

                if abs(target - total) < min_diff:
                    min_diff = abs(target - total)
                    closest_total = total

        return closest_total
