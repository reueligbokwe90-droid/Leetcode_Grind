class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in range(len(numbers)):
            for y in range(1,len(numbers)):
                if numbers[x] + numbers[y] == target:
                    return [x+1,y+1] 
        return []
        