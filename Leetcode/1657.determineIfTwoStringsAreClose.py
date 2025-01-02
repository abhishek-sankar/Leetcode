class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a_count = Counter(word1)
        b_count = Counter(word2)

        a_arr = sorted([count for count in a_count.values()])
        b_arr = sorted([count for count in b_count.values()])

        a_uniques = sorted([key for key in a_count.keys()])
        b_uniques = sorted([key for key in b_count.keys()])

        return (
            all(a == b for a, b in zip(a_arr, b_arr))
            and all(a == b for a, b in zip(a_uniques, b_uniques))
            and len(word1) == len(word2)
        )
