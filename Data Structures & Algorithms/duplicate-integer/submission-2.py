class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input - list of number
        #process - seen dictionsry - record all the the seen elements in the array
        # loop throught the nums array
        # chcek if the element is already in the seen.
        # if it isnt(else) - add to the seen dict
        #ouput - boolean t/f if duplicate is found
        # seen = {1,2,3} return true
        seen = {}
        for number in nums:
            if number in seen:
                return True
            else:
                seen[number] = seen.get(number,0)
        return False
            


    