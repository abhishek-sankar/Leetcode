class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev = 0
        for index in spaces:
            res.append(s[prev: index])
            prev = index
        res.append(s[prev:])
        return " ".join(res)