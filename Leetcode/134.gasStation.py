class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starting_indices = [i for i in range(len(gas)) if gas[i] >= cost[i]]
        n = len(gas)

        start = 0
        total_gas = 0
        total_cost = 0
        tank = 0
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= total_cost else -1
