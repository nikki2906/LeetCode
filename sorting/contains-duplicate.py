class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        