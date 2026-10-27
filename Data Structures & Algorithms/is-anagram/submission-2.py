class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = sorted(s)
        q = sorted(t)

        if len(q) != len(q):
            return False

        if q == p:
            return True
        else:
            return False