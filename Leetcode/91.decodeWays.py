class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s) + [1]

        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                    dp[i] += dp[i+2]     
            else:
                dp[i] = 0           
        return dp[0]

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(index):
            if index in dp:
                return dp[index]
            if s[index] == '0':
                return 0
            res = dfs(index + 1)
            if index + 1 < len(s) and (s[index] == '1' or s[index] == '2' and s[index + 1] in '0123456'):
                res += dfs(index + 2)
            dp[index] = res
            return res
        return dfs(0)
'''