class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindrome(l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return (r - l - 1) // 2
        
        count = 0
        for i in range(len(s)):
            count += checkPalindrome(i, i) + checkPalindrome(i, i + 1)
        
        return len(s) + count