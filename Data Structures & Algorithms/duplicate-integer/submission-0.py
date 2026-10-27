class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = {}
        for x in nums:
            if x in memory:
                return True
            else:
                memory[x] = x
        return False