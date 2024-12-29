class Solution:
    def grayCode(self, n: int) -> List[int]:
        def getGrayCode(index):
            if index == 1:
                return ["0", "1"]
            prevCode = getGrayCode(index - 1)
            first = []
            second = []
            for code in prevCode:
                first.append("0" + code)
                second.append("1" + code)
            return [*first, *second[::-1]]

        def convertGrayStringToNumbers(grayCodes):
            return [int(code, 2) for code in grayCodes]

        return convertGrayStringToNumbers(getGrayCode(n))
