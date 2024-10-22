class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0 # reset to 0
            # add the current number to the curr sum
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub
        