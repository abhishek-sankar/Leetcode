class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score = max(
                score,
                sum(1 for x in s[: i + 1] if x == "0")
                + sum(1 for x in s[i + 1 :] if x == "1"),
            )

        return score
