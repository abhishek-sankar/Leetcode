class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            # "0": [" "],
            # "1": []
        }

        def dfs(i, current):
            if i == len(digits):
                if len(current) > 0:
                    res.append(current)
                return
            if i > len(digits):
                return

            for letter in mapping[digits[i]]:
                dfs(i + 1, current + letter)

        dfs(0, "")

        return res