class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        longer, shorter = (s, t) if len(s) >= len(t) else (t, s)
        for i in range(len(longer)):
            s_d[longer[i]] = s_d.get(longer[i], 0) + 1
        for i in range(len(shorter)):
            s_d[shorter[i]] = s_d.get(shorter[i], 0) - 1
        
        return max(s_d.values()) == 0