class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        def processToken(val1, val2, operator):
            if operator == "+":
                return val1 + val2
            if operator == "-":
                return val1 - val2
            if operator == "*":
                return val1 * val2
            if operator == "/":
                return int(val1 / val2)

        for token in tokens:
            if token in "+-*/":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(processToken(int(operand_1), int(operand_2), token))
            else:
                stack.append(int(token))

        return stack[-1]
