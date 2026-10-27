class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(len(nums)):
            item = nums.pop(x)
            prod = 1
            for n in nums:
                prod *= n
            res.append(prod)
            nums.insert(x,item)
        return res