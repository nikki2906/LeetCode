class Solution(object):
    def isValid(self, s):
        hashMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        # don't need the indices because you are not working with index
        for char in s:
            if char not in hashMap: 
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack.pop() != hashMap[char]:
                    return False
        return True if not stack else False