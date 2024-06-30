class Solution(object):
    def isValid(self, s):
        stack = []
        hashMap = {'}': '{', ']': '[', ')' : '('}
        for c in s:
            if c not in hashMap:
                stack.append(c)
            elif stack and hashMap[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False