class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1 
        while left < right:
            area = min(height[right], height[left]) * (right - left)
            max_area = max(area, max_area)
            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area
        