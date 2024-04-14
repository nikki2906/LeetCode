class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # set up
        left = 0
        length = 0
        charSet = set()
        # the bulk
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            while s[right] not in charSet:
                charSet.add(s[right])
                length = max(length, right - left + 1)
        return length