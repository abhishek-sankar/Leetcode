class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count, start = 0, 0
        substrings = []
        for i in range(len(s)):
            count += 1 if s[i] == "1" else -1

            if count == 0:
                substrings.append("1" + self.makeLargestSpecial(s[start + 1 : i]) + "0")
                start = i + 1
        substrings.sort(reverse=True)

        return "".join(substrings)
