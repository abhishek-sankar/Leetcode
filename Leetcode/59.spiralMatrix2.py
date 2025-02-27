class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        t, l = 0, 0
        b, r = n - 1, n - 1

        k = 1
        while k <= n * n:
            for i in range(l, r + 1):
                matrix[t][i] = k
                k += 1
            t += 1
            # print(matrix)

            for i in range(t, b + 1):
                matrix[i][r] = k
                k += 1
            r -= 1
            # print(matrix)

            for i in range(r, l - 1, -1):
                matrix[b][i] = k
                k += 1
            b -= 1
            # print(matrix)

            for i in range(b, t - 1, -1):
                matrix[i][l] = k
                k += 1
            l += 1
            # print(matrix)

        return matrix
