class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        res = 0
        hashSet = set()
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right]) 
            res = max(res, right - left + 1)
        return res
        