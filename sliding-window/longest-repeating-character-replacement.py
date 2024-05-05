class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        count = {}
        mostFreq = 0
        for right in range(len(s)):
            count[s[right]] =  1 + count.get(s[right], 0)
            mostFreq = max(mostFreq, count[s[right]])
            while (right - left + 1) - mostFreq > k:
                count[s[left]] -= 1
                left += 1
        return (right - left + 1)        