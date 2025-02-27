class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1

            if l == r:
                longest = max(longest, 2 * l)
            if r > l:
                l = 0
                r = 0
        l = 0
        r = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                l += 1
            else:
                r += 1

            if l == r:
                longest = max(longest, 2 * l)
            if r > l:
                l = 0
                r = 0

        return longest
