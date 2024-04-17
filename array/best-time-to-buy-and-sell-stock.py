class Solution(object):
    def maxProfit(self, prices):
        # buy low sell high
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            elif prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            right += 1
        return max_profit