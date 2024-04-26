class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target -  num
            if difference not in hashMap:
                hashMap[num] =  i
            else:
                return (hashMap[difference], i)      
                