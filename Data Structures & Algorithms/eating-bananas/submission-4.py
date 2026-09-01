class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        result = r
        while l <= r:
            m = (l + r) // 2
            
            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile) / m)
            
            if total_time <= h:
                result = m
                r = m - 1
            else:
                l = m + 1
        return result 