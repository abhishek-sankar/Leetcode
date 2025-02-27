class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        dict = {x: "" for x in range(numRows)}
        for i in range(len(s)):
            pos = i % (2 * numRows - 2)
            if pos > numRows - 1:
                pos = numRows - 1 - abs(numRows - 1 - pos)
            dict[pos] += s[i]

        res = ""
        for i in range(numRows):
            res += dict[i]
        return res
