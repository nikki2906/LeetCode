class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_curr = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_curr = max(max_curr, profit)
            else:
                left = right
            right += 1
        return max_curr