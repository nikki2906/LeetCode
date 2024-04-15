class Solution(object):
    def isPalindrome(self, s):
        # set up
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            if s[right].lower() != s[left].lower():
                return False
            right -= 1
            left += 1
        return True

    def isAlphanumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9"))
        