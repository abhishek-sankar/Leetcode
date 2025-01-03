class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if ch == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(list(stack))
