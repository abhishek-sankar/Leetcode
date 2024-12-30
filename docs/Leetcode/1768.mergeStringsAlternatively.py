class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s, l = (word1, word2)
        #  if len(word1) < len(word2) else (word2, word1)
        res = ""
        i = 0
        for i in range(min(len(s), len(l))):
            res += s[i] + l[i]

        if i == len(s) - 1:
            for i in range(len(s), len(l)):
                res += l[i]
        else:
            for i in range(len(l), len(s)):
                res += s[i]

        return res
