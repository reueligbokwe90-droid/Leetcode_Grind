class Solution:
    def isValid(self, s: str) -> bool:
        memo = {")":"(", "}":"{", "]":"["}
        res = []

        for char in s:
            if char in memo:
                if res and memo[char] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)

        return True if not res else False