class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            elif prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            right += 1
        return maxProfit