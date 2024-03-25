class Solution(object):
    def myPow(self, x, n):
        # Break into base case where n = 0 or n = 1 or n = -1
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        
        # recurrent relations where n is even or odd numbers.
        result = self.myPow(x, n // 2)

        return result * result * (x if n % 2 else 1)