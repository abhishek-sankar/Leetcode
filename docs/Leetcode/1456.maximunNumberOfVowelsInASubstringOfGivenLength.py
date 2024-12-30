class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        max_vowels = sum([1 for char in s[:k] if char in vowels])
        current = max_vowels
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current -= 1
            if s[i] in vowels:
                current += 1
            max_vowels = max(max_vowels, current)

        return max_vowels
