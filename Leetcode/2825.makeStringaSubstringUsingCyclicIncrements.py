class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1, s2 = 0, 0
        while s1 < len(str1):
            if s2 == len(str2):
                return True
            if str1[s1] != str2[s2] and (ord(str1[s1]) - ord('a') + 1) % 26 != (ord(str2[s2]) - ord('a')) % 26:
                print(ord(str1[s1]) + 1, str1[s1], str2[s2])
                s1 += 1
            else:
                s1 += 1
                s2 += 1

        if s2 == len(str2):
            return True
        return False