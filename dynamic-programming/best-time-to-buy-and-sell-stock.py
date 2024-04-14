class Solution(object):
    def maxProfit(self, prices):
        # set up
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            right += 1
        return max_profit
        