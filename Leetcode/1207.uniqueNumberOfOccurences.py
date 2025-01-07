class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        return len(set(counter.values())) == len(counter.values())
