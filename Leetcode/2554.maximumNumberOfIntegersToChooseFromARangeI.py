class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        total = 0
        count = 0
        for i in range(1, n+1):
            if i not in ban:
                if total + i > maxSum:
                    return count
                else:
                    total += i
                    count += 1
                    
        return count