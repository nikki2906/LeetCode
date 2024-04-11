class Solution(object):
    def threeSum(self, nums):
        # set up
        res = []
        nums.sort()

        # first num: check for duplicate value -> skip
        for i, a in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue 
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                # two sum
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
            