class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        mod = 10 ** 9 + 7
        power = 1
        last_index = 0

        for i in range(len(s)):
            char = (ord(s[i]) - ord('a') + 1)
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            
            power = (power * base) % mod
        
            if prefix == suffix:
                last_index = i
        
        return s[last_index + 1: ][::-1] + s

