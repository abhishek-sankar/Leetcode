class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        res = [(x[0] in vowels and x[-1] in vowels) for x in words]
        prefix = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix[i + 1] = prefix[i] + (1 if res[i] == True else 0)
        return [(prefix[end + 1] - prefix[start]) for [start, end] in queries]
