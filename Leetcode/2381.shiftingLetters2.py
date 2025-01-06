class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        starts = [0] * (len(s) + 1)
        ends = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            starts[start] += 1 if direction == 1 else -1
            starts[end + 1] += -1 if direction == 1 else 1

        prefix_sum = [0] * (len(s) + 1)
        for i in range(len(s)):
            prefix_sum[i + 1] = prefix_sum[i] + starts[i]
        letters = list(s)
        letters = [ord(ch) - ord("a") for ch in letters]

        res = [
            chr((l + shift) % 26 + ord("a"))
            for l, shift in zip(letters, prefix_sum[1:])
        ]

        return "".join(res)


# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
#         shift_results = [0] * len(s)
#         for start, end, direction in shifts:
#             shift_results[start:end+1] = [(x + (1 if direction == 1 else -1)) for x in shift_results[start:end+1]]
#         shift_results = [chr((ord(s[i]) - ord('a') + x) % 26 + ord('a')) for i, x in enumerate(shift_results)]
#         return "".join(shift_results)
