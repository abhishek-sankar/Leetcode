class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return max(n, 1)
        MOD = 1000000007
        f = [0] * (n + 1)
        s = [0] * (n + 1)

        f[0], f[1] = 1, 1
        s[0] = 0

        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + 2 * s[i - 1]) % MOD
            s[i] = (f[i - 2] + s[i - 1]) % MOD

        return f[n] % MOD
