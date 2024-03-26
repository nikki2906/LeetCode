class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)
            if hours <= h:
                res = k
                right = k - 1 
            else:
                left = k + 1
        return res