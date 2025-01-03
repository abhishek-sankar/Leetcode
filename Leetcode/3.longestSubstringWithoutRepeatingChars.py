class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        cur_set = set()
        max_len = float("-inf")
        while r < len(s):
            if s[r] in cur_set:
                while s[r] in cur_set:
                    cur_set.remove(s[l])
                    l += 1
            max_len = max(max_len, r - l + 1)
            cur_set.add(s[r])
            r += 1
        
        return max_len