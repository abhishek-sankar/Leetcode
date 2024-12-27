class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)

        def permute(s):
            if len(s) == 1:
                return [s]
            char = s[0]
            prev = permute(s[1:])
            current = []
            for perm in prev:
                for i in range(len(perm) + 1):
                    if i > 0 and perm[i - 1] == char:
                        break
                    # print(perm[:i] + [char] + perm[i:], i)
                    current.append(perm[:i] + [char] + perm[i:])
            # print(current)
            return current

        return permute(nums)
