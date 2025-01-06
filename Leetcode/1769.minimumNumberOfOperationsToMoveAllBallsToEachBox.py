class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices = list(boxes)
        n = len(indices)
        return [
            sum([abs(x - i) for (x, j) in enumerate(indices) if j == "1"])
            for i in range(n)
        ]
