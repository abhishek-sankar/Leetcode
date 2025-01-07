class Solution:
    def countBits(self, n: int) -> List[int]:
        def getPrevArr(index):
            if index == 0:
                return [0]
            if index == 1:
                return [0, 1]

            prevIndexArray = getPrevArr(index - 1)
            doubled = [1 + count for count in prevIndexArray]
            return prevIndexArray + doubled

        start = 1
        count = 0
        while True:
            start *= 2
            count += 1
            if start >= n + 1:
                break

        res = getPrevArr(count)
        return res[: n + 1]
