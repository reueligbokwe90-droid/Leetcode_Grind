class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        memo = set()

        for r in range(len(s)):
            while s[r] in memo:
                memo.remove(s[l])
                l += 1
            memo.add(s[r])
            length = max(length, (r - l) + 1)
        return length
