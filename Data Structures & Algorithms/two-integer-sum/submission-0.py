class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for x in range(len(nums)):
            complement = target - nums[x]
            if complement in memo:
                return[memo[complement],x]
            memo[nums[x]] = x
        return[]