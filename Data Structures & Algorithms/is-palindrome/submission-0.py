class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        s = "".join(res)
        return s == s[::-1]
        

