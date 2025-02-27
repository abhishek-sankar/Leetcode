class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque([i for i, senator in enumerate(senate) if senator == "R"])
        d_q = deque([i for i, senator in enumerate(senate) if senator == "D"])

        index_count = len(senate)

        while r_q and d_q:
            r_senator = r_q.popleft()
            d_senator = d_q.popleft()
            if r_senator < d_senator:
                index_count += 1
                r_q.append(index_count)
            else:
                index_count += 1
                d_q.append(index_count)
        
        return "Radiant" if r_q else "Dire"
