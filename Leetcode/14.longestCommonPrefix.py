class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        lengths = [len(s) for s in strs]
        lowest = min(lengths)
        flag = False
        for idx in range(lowest):
            current = strs[0][idx]
            for s in strs:
                if s[idx] != current:
                    flag = True
                    idx -= 1
                    break
            if flag:
                break
        return strs[0][: idx + 1] if lowest > 0 else ""
