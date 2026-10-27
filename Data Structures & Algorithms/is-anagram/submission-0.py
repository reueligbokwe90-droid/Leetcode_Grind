class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t,s = sorted(t), sorted(s)
        if t == s:
            return True
        return False
        