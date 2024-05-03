class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        left = 0
        right = 1
        while right < len(prices):
            if  prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
        