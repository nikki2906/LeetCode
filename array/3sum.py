class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + a
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
    