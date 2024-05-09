class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for index, temp  in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return res
        