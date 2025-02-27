class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if any(word in _word for _word in words if _word != word):
                res.append(word)
        return res
