class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        res = 0
        for x in range (len(prices)):
            for y in range (x+1, len(prices)):
                if prices[x] > prices[y]:
                    res = 0
                res = prices[y] - prices[x]
                current_max = max(current_max, res)
        return current_max
        