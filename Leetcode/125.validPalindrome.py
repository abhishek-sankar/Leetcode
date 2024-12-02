class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_str = s.lower()
        string = "".join([char for char in lowercase_str if char.isalnum()])
        return string == string[::-1]