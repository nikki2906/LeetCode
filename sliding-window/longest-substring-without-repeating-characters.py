class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # detect duplicate -> hash set
        left = 0
        max_length = 0
        charSet = set()
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            while s[right] not in charSet:
                charSet.add(s[right])
                max_length = max(max_length, right - left + 1)
        return max_length
        