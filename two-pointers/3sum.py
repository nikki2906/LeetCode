class Solution(object):
    def threeSum(self, nums):
        # set up
        res = [] # a list
        nums.sort()

        # first num
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # second num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[right], nums[left]])
                    left += 1
                    
                    # shift the pointer
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                    while nums[right - 1] == nums[right] and left < right:
                        right -= 1
        return res