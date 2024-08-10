class Solution(object):
    def containsDuplicate(self, nums):
        hashMap = set()
        for num in nums:
            if num not in hashMap:
                hashMap.add(num)
            else:
                return True
        return False
        