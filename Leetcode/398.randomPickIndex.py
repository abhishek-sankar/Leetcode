class Solution:

    def __init__(self, nums: List[int]):
        self.map = {}
        for idx, nums in enumerate(nums):
            if nums not in self.map:
                self.map[nums] = []
            self.map[nums].append(idx)

    def pick(self, target: int) -> int:
        if target in self.map:
            return random.choice(self.map[target])
        else:
            return None


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)