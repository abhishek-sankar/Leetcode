class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x for x in reversed([y for y in s.split(" ") if y != ""])])
