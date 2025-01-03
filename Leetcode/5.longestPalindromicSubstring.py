class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(l, r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return r - l - 1

        longest = ""
        for i in range(len(s)):
            center = checkPalindrome(i, i)
            acenter = checkPalindrome(i, i+1)
            max_len = max(center, acenter)

            if max_len > len(longest):
                longest = s[i - (max_len - 1)// 2: i + max_len // 2 + 1]
        
        return longest
                
