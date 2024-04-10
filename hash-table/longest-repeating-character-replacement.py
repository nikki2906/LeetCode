class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(count[s[right]], max_freq)
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

        return (right - left + 1)