class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        remaining = Counter(nums)
        total = 0
        for item, count in remaining.items():
            if (target - item) in remaining:
                if target == 2 * item:
                    total += remaining[item] // 2
                    remaining[item] = 0
                else:
                    total += min(remaining[item], remaining[target - item])
                    remaining[item] = 0
                    remaining[target - item] = 0
        return total
