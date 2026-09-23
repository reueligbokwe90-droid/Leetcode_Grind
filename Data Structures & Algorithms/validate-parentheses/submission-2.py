class Solution:
    def isValid(self, s: str) -> bool:
        order = {")":"(", "}":"{", "]":"["}
        res = []

        for char in s:
            if char in order:
                if res and res[-1] == order[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        return True if not res else False