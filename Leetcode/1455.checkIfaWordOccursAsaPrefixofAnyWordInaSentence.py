class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent = sentence.split(" ")
        res = [idx for idx, s in enumerate(sent) if s.startswith(searchWord)]

        if res:
            return res[0] + 1
        return -1