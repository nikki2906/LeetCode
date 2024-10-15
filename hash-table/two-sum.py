class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference not in hashMap:
                hashMap[num] = i
            else:
                return(hashMap[difference], i)