class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        charSet = set()
        length = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            while s[right] not in charSet:
                charSet.add(s[right])
                length = max(length, right - left + 1)
        return length 
        