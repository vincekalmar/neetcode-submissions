class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        l = 0
        res = 0

        for r in range(n):
            if prices[l] < prices[r]:
                res = max(prices[r] - prices[l], res)
            else:
                l=r
        return res

