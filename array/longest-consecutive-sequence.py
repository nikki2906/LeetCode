class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in hashSet:
                count = 0
                while (num + count) in hashSet:
                    count += 1
                longest = max(count, longest)
        return longest
        