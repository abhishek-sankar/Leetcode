class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        front_heap = []
        back_heap = []
        total_costs = 0

        f, b = 0, len(costs) - 1
        while f < candidates and f <= b:
            heapq.heappush(front_heap, costs[f])
            f += 1

        while b >= len(costs) - candidates and b >= f:
            heapq.heappush(back_heap, costs[b])
            b -= 1

        total_cost = 0
        for _ in range(k):
            if front_heap and back_heap:
                if front_heap[0] <= back_heap[0]:
                    total_costs += heapq.heappop(front_heap)
                    if f <= b:
                        heapq.heappush(front_heap, costs[f])
                        f += 1
                else:
                    total_costs += heapq.heappop(back_heap)
                    if b >= f:
                        heapq.heappush(back_heap, costs[b])
                        b -= 1
            elif front_heap:
                total_costs += heapq.heappop(front_heap)
                if f <= b:
                    heapq.heappush(front_heap, costs[f])
                    f += 1
            elif back_heap:
                total_costs += heapq.heappop(back_heap)
                if b >= f:
                    heapq.heappush(back_heap, costs[b])
                    b -= 1

        return total_costs
