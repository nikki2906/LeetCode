class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        charSet = set()
        curr_max = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            while s[right] not in charSet:
                charSet.add(s[right])
                curr_max = max(curr_max, right - left + 1) # right - left + 1: gives the current window size
        return curr_max