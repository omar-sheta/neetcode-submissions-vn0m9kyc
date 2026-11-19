class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep a window of period with max profit.
        # slide it by one if profit is dec.
        # expand it by one to the right if prof is inc.

        l = 0
        r = 1

        max_profit = 0

        while r <= len(prices) - 1:
            profit = prices[r] - prices[l]
            if profit>=0:
                max_profit = max(max_profit,profit)
                r+=1
            else:
                l+=1
                r = l+1
        
        return max_profit