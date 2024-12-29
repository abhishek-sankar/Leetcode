class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pool = [str(i) for i in range(1, n + 1)]

        res = ""
        k -= 1

        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)

            next_number = k // fact
            res += pool.pop(next_number)

            k %= fact

        return res
