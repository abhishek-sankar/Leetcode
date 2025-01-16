class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText) // rows
        mat = []
        for i in range(rows):
            mat.append(encodedText[i * n : (i + 1) * n])
        res = []
        for i in range(n):
            for j in range(rows):
                if i + j < n:
                    res.append(mat[j][i + j])

        return "".join(res).rstrip()
