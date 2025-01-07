class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, citation in enumerate(citations):
            if i + 1 > citations[i]:
                return i

        return len(citations)
