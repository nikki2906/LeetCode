class Solution(object):
    def integerReplacement(self, n):
        if n == 1:
            return 0
        ops = 0
        while n > 1:
            if n & 1 == 0:
                n = n // 2
                ops = ops + 1
            elif n == 3:
                n = n - 1
                ops = ops + 1
            else:
                if (n-1) // 2 & 1 == 0:
                    n = n - 1
                    ops = ops + 1
                else:
                    n = n + 1
                    ops = ops + 1
        return ops