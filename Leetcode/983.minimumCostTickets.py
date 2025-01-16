class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travelDays = [False] * (max(days) + 1)
        travelCost = [0] * (max(days) + 1)
        for day in days:
            travelDays[day] = True

        for i in range(len(travelCost)):
            # print(i)
            travelCost[i] = (
                min(
                    travelCost[max(i - 1, 0)] + costs[0],
                    travelCost[max(i - 7, 0)] + costs[1],
                    travelCost[max(i - 30, 0)] + costs[2],
                )
                if travelDays[i]
                else travelCost[max(i - 1, 0)]
            )

        return travelCost[-1]
