class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        # first number
        for i, a in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else: 
                    res.append([a, nums[left], nums[right]])
                    left += 1

                    # shift the pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res        