class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def getPascalRow(index):
            if index in cache:
                return cache[index]
            else:
                prevRow = getPascalRow(index - 1)
                res = [1]
                for i in range(len(prevRow) - 1):
                    res.append(prevRow[i] + prevRow[i + 1])
                res.append(1)
                cache[index] = res
                return cache[index]

        cache = {0: [1], 1: [1, 1]}

        return getPascalRow(rowIndex)
