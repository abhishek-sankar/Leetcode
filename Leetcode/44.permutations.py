class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def perms(s):
            if len(s) == 1:
                return [s]

            prevPermutations = perms(s[1:])
            char = s[0]
            current = []
            for i in range(len(prevPermutations)):
                for j in range(len(prevPermutations[i]) + 1):
                    current.append(
                        prevPermutations[i][:j] + [char] + prevPermutations[i][j:]
                    )
            # print(current)
            return current

        res = perms(nums)

        return res
