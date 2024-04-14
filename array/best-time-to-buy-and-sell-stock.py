class Solution(object):
    def maxProfit(self, prices):
        left = 0 # buy
        right = 1 # sell
        max_profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            right += 1
        return max_profit
        