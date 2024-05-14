class Solution(object):
    def threeSum(self, nums):
        # set up
        res = []
        nums.sort()

        # 1st integer
        for i, a in enumerate(nums):
            if nums[i-1] == nums[i] and i>0:
                continue
            # 2nd and 3rd integers
            left = i+1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left-1] == nums[left] and left < right:
                        left += 1
        return res
        