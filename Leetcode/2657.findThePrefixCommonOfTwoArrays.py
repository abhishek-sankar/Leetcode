class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        n = len(A)
        C = [0] * n
        for i in range(n):
            a.add(A[i])
            b.add(B[i])
            C[i] = len(a & b)

        return C
