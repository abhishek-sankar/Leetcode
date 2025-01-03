class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(base, exponent):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                return power(base * base, exponent / 2)
            else:
                return base * power(base * base, (exponent - 1) / 2)

        return power(x, n) if n > 0 else power(1 / x, -n)
