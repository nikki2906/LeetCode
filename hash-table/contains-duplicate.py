class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()
        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
            else: 
                return True
        return False