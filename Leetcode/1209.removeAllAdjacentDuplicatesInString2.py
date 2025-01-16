class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        stack.append(["#", 0])
        for i in range(len(s)):
            if stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    continue
            else:
                stack.append([s[i], 1])

        return "".join([c * i for c, i in stack])
