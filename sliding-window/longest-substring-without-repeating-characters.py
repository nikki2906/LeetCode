class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxFreq = 0
        hashSet = set()
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            maxFreq = max(right - left + 1, maxFreq)
        return maxFreq
        