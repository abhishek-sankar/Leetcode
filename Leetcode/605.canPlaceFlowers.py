class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r = 0
        while n and r < len(flowerbed):
            if flowerbed[r] == 0:
                if (r == 0 or flowerbed[r - 1] == 0) and (
                    r == len(flowerbed) - 1 or flowerbed[r + 1] == 0
                ):
                    n -= 1
                    r += 1
            r += 1
        return n == 0
