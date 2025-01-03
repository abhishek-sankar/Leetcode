class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        word_counts = Counter(words)
        total_count = len(words)

        res = []

        for i in range(length):
            start = i
            count = 0
            current_count = defaultdict(int)
            for j in range(i, len(s) - length + 1, length):
                word = s[j : j + length]
                if word not in word_counts:
                    current_count.clear()
                    start = j + length
                    count = 0
                    continue
                    # reset dict, count, set start ahead, dont process word
                current_count[word] = current_count.get(word, 0) + 1
                count += 1
                while current_count[word] > word_counts[word]:
                    current_count[s[start : start + length]] -= 1
                    start += length
                    count -= 1
                if count == total_count:
                    res.append(start)

        return res


# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         # create a count dict
#         # init left and right
#         # init a current_count dict
#         # start at 0, 0 and move forward l chars
#         # if matches word, update current_count, and count
#         # if count == word_count, add index to result
#         # if current count of word is greater than expected, move left forward
#         # if no match, reset count and current count
#         count_dict = {}
#         for word in words:
#             count_dict[word] = count_dict.get(word, 0) + 1
#         res = set()
#         word_len = len(words[0])
#         total_words = len(words)

#         for i in range(len(s)):
#             l, r = i, i
#             count = 0
#             current_dict = {}
#             while r + word_len <= len(s):
#                 next_word = s[r : r + word_len]
#                 r += word_len
#                 if next_word in count_dict:
#                     current_dict[next_word] = current_dict.get(next_word, 0) + 1
#                     count += 1
#                     while current_dict[next_word] > count_dict[next_word]:
#                         word_to_drop = s[l : l + word_len]
#                         current_dict[word_to_drop] -= 1
#                         l += word_len
#                         count -= 1
#                         # print("drop", count, word_to_drop, current_dict)
#                     if count == total_words:
#                         res.add(l)
#                 else:
#                     count = 0
#                     current_dict.clear()
#                     l = r
#         return list(res)
