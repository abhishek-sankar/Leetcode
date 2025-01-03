class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        res = 0
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            num_res = 0
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                num_res += ((int(num2[j]) * int(num1[i]) + carry) % 10) * pow(
                    10, len(num2) - j - 1 + len(num1) - i - 1
                )
                carry = (int(num2[j]) * int(num1[i]) + carry) // 10
                print(num_res, carry)
            res += num_res + carry * pow(10, len(num2) + len(num1) - i - 1)
            # print(num_res + carry * pow(10, len(num2) + len(num1) - i - 1))
        return str(res)
