class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        pairs = [i for i, x in enumerate(s) if x in vowels]
        s = list(s)
        l, r = 0, len(pairs) - 1
        while l < r:
            s[pairs[l]], s[pairs[r]] = s[pairs[r]], s[pairs[l]]
            l += 1
            r -= 1

        return "".join(s)
