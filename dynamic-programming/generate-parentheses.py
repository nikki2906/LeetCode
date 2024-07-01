class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append(''.join(stack))
                return 
            if openCount > closedCount:
                stack.append(')')
                backtrack(openCount, closedCount + 1)
                stack.pop()
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closedCount)
                stack.pop()
        backtrack(0, 0)
        return res