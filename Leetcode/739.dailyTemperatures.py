class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer = [0] * len(temperatures)

        s = deque()
        s.append((0, temperatures[0]))
        for i, temp in enumerate(temperatures[1:]):
            if s and temp > s[-1][1]:
                while s and temp > s[-1][1]:
                    idx, _temp = s.pop()
                    warmer[idx] = i + 1 - idx

            s.append((i + 1, temp))
        return warmer
