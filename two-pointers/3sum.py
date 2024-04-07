class Solution(object):
    def threeSum(self, nums):
        # set up the problem
        res = []
        nums.sort()
        # check for neighbors
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue        
            # set up ptrs
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
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res  