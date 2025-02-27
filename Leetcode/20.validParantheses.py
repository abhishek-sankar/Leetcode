from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()

        openers = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in ['(', '[', '{']:
                d.append(char)
            elif char in openers:
                if not d or d[-1] != openers[char]:
                    return False
                else:
                    d.pop()
        if len(d) == 0:
            return True
        return False