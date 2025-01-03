class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            res[tuple(counts)].append(s)

        return [value for value in res.values()]
