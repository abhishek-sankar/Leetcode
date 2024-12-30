class Solution:
    def compress(self, chars: List[str]) -> int:
        char = chars[0]
        res = ""
        current_count = 1
        for i, c in enumerate(chars[1:]):
            print(res)
            if char == c:
                current_count += 1
            else:
                res += char
                if current_count > 1:
                    res += str(current_count)
                char = c
                current_count = 1
        res += char
        if current_count > 1:
            res += str(current_count)
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
