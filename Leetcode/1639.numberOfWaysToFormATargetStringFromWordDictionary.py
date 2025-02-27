class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        word_length = len(words[0])
        target_length = len(target)
        freq = [[0] * 26 for _ in range(word_length)]
        MOD = 1000000007

        for word in words:
            for i, ch in enumerate(word):
                freq[i][ord(ch) - ord("a")] += 1

        # width = word_length - target_length + 1

        cache = {}

        def backtrack(word_index, target_index):
            if target_index == target_length:
                return 1
            if word_index == word_length:
                return 0

            if (word_index, target_index) in cache:
                return cache[(word_index, target_index)]

            target_char = target[target_index]

            ways = backtrack(word_index + 1, target_index)

            if freq[word_index][ord(target_char) - ord("a")] > 0:
                ways += freq[word_index][ord(target_char) - ord("a")] * backtrack(
                    word_index + 1, target_index + 1
                )
                ways %= MOD

            cache[(word_index, target_index)] = ways
            return ways

        total_ways = backtrack(0, 0)
        return total_ways
