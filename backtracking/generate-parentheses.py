class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        
        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closedCount)
                stack.pop()
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res