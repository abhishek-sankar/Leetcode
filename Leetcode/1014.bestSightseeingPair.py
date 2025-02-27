class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2:
            return sum(values) - 1
        add = [x + i for i, x in enumerate(values)]
        sub = [x - i for i, x in enumerate(values)]
        # print(add, sub)
        max_so_far = float("-inf")
        add_max = []
        for num in add:
            max_so_far = max(max_so_far, num)
            add_max.append(max_so_far)

        max_so_far = float("-inf")
        sub_max = [max_so_far] * len(sub)
        for i in range(len(sub) - 1, -1, -1):
            max_so_far = max(max_so_far, sub[i])
            sub_max[i] = max_so_far

        total_max = float("-inf")
        for i in range(len(values) - 1):
            total_max = max(total_max, add_max[i] + sub_max[i + 1])

        # print(add_max, sub_max)
        return total_max
