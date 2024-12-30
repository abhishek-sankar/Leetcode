class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def checkGCD(s1, s2):
            div_len = len(s2)
            str_len = len(s1)
            if str_len % div_len != 0:
                return False
            for i in range(len(s1)):
                if s1[i] != s2[i % div_len]:
                    return False
            return True

        s, l = (str1, str2) if len(str1) < len(str2) else (str2, str1)

        res = ""
        for i in range(len(s)):
            if checkGCD(s, s[: i + 1]) and checkGCD(l, s[: i + 1]):
                res = s[: i + 1]

        return res
