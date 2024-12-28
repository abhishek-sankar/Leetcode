class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(index, current, dots):
            if dots == 3:
                if isValid(s[index:]):
                    res.append(current + s[index:])

            for i in range(1, 4):
                segment = s[index : index + i]
                if isValid(segment):
                    backtrack(index + i, current + segment + ".", dots + 1)

        def isValid(segment):
            if len(segment) == 0 or len(segment) > 3:
                return False
            if segment[0] == "0":
                return len(segment) == 1
            if int(segment) > 255:
                return False

            return True

        backtrack(0, "", 0)
        return res