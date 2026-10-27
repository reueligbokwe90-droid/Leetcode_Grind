class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for x in range(len(numbers)):
            complement = target - numbers[x]
            if complement in memo:
                return[memo[complement] +1,x +1]
            memo[numbers[x]] = x
            
        