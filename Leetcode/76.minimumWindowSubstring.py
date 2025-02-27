class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        need_map = {}

        for char in t:
            need_map[char] = need_map.get(char, 0) + 1
        
        have_map = {}
        have, need = 0, len(need_map)

        l, min_l = 0, float("inf")
        min_string = ""

        for r in range(len(s)):
            if s[r] in need_map:
                have_map[s[r]] = have_map.get(s[r], 0) + 1
                if have_map[s[r]] == need_map[s[r]]:
                    have += 1
            
            while have == need:
                if r - l + 1 < min_l:
                    min_l = r-l+1
                    min_string = s[l:r+1]

                if s[l] in need_map:
                    if have_map[s[l]] == need_map[s[l]]:
                        have -= 1
                    have_map[s[l]] = have_map.get(s[l]) - 1
                
                l += 1
        return min_string

                


