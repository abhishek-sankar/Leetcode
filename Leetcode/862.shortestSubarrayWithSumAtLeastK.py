class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = deque()
        shortest = float("inf")
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n + 1):
            while dq and (prefix[i] - prefix[dq[0]]) >= k:
                shortest = min(shortest, i - dq.popleft())
            
            while dq and prefix[i] < prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return shortest if shortest != float("inf") else -1