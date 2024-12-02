class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = {}
        max_len = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -=1
                l += 1
            max_len = max(max_len, r - l + 1)
            
        return max_len
