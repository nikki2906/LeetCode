class Solution(object):
    def maxProfit(self, prices):
        left = 0
        max_profit = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit