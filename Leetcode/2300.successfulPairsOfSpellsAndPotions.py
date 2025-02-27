class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        pairs = [0] * len(spells)

        potions.sort()

        needed_min = [ceil(success / spell) for spell in spells]

        def binarySearch(val):
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] >= val:
                    r = mid - 1
                else:
                    l = mid + 1

            return len(potions) - l

        return [binarySearch(value) for value in needed_min]
