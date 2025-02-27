class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurence = {}
        last_occurence = {}
        MOD = 1000000007
        total_palindromes = 0

        for i, ch in enumerate(s):
            if ch not in first_occurence:
                first_occurence[ch] = i
            last_occurence[ch] = i

        for letter in first_occurence.keys():
            # find gap till last occurence
            # r - l - 1
            # take a set of all the letters of s in between for diff possible middle chars
            middle_letters = set(
                s[first_occurence[letter] + 1 : last_occurence[letter]]
            )
            total_palindromes = (total_palindromes + len(middle_letters)) % MOD

        return total_palindromes % MOD


# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         uniques = set()
#         sequence = list(s)

#         def backtrack(index, current, l):
#             # print(index, current)
#             if index > len(s):
#                 return
#             if l == 3:
#                 uniques.add("".join(current))
#             # if len(current) > 3:
#             #     return
#             if l <= 1:
#                 for i in range(index, len(s)):
#                     current.append(sequence[i])
#                     backtrack(i + 1, current, l + 1)
#                     current.pop()
#             elif l == 2:
#                 for i in range(index, len(s)):
#                     if s[i] == current[0]:
#                         current.append(sequence[i])
#                         backtrack(i + 1, current, l + 1)
#                         current.pop()

#         def checkPalindrome(seq):
#             return seq[0] == seq[-1]

#         backtrack(0, [], 0)
#         return len(uniques)
