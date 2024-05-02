class Solution(object):
    def longestConsecutive(self, nums):
        hashSet =set(nums)
        longest = 0
        for num in hashSet:
            if (num - 1) not in hashSet:
                length = 0
                while (num + length) in hashSet:
                    length += 1
                longest = max(length, longest)
        return longest