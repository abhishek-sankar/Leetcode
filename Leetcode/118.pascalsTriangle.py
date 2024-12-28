class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
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

        cache = {1: [1], 2: [1, 1]}

        result = []
        for i in range(1, numRows + 1):
            result.append(getPascalRow(i))
        return result
