class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = deque()

        for i, ch in enumerate(s):
            if ch != "]":
                stack.append(ch)
            else:
                # print(s[:i], s[i:])
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                else:
                    stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                string = int(num) * string
                for ch in string:
                    stack.append(ch)
        return "".join(list(stack))
