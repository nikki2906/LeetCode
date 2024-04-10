class Solution(object):
    def characterReplacement(self, s, k):
        # set up
        left = 0
        count = {}
        res = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            res = max(res, count[s[right]])
            while (right - left + 1) - res > k:
                count[s[left]] -= 1
                left += 1
        return (right - left + 1)