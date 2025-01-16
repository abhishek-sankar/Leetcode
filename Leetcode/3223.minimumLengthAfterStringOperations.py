class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        return sum([1 if count % 2 != 0 else 2 for count in counts.values()])
