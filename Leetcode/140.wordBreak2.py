class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        def backtrack(index, current):
            if index == len(s):
                res.append(" ".join(current))
                return
            
            for i in range(index, len(s)):
                if s[index:i + 1] in wordDict:
                    current.append(s[index:i + 1])
                    backtrack(i+1, current)
                    current.pop()
        
        backtrack(0, [])
        return res
            
