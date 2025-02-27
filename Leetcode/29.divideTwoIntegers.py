class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        D, d = abs(dividend), abs(divisor)
        res = 0
        while D >= d:
            p = 0
            while D - (d << 1 << p) >= 0:
                p += 1
            res += 1 << p
            D -= d << p
        res = res * sign
        return min(max(-1 * pow(2, 31), res), pow(2, 31) - 1)
