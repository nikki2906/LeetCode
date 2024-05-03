class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right: 
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1  # Corrected here
                right -= 1  # Corrected here
        return maxArea
        