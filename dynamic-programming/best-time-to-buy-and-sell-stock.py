class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        currMax = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                currMax = max(profit, currMax)
            else: 
                left = right
            right += 1
        return currMax
    
        