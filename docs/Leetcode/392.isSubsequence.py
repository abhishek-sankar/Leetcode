class Solution:
    def isSubsequence(self, se: str, t: str) -> bool:
        big, small = 0, 0
        while small < len(se) and big < len(t):
            if se[small] == t[big]:
                big += 1
                small += 1
            else:
                big += 1

        return small == len(se)
