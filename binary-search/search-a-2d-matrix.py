class Solution(object):
    def searchMatrix(self, matrix, target):
        # get the dimension:
        rows = len(matrix)
        cols = len(matrix[0])

        # get the mid row 
        top = 0
        bottom = rows - 1
        while top <= bottom: 
            midRow = (top + bottom) // 2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            else:
                break
        
            if not(top <= bottom):
                return False
        
        # get the mid point
        left = 0
        right = cols - 1
        midRow = (top + bottom) // 2
        while left <= right:
            mid = (left + right) // 2
            if matrix[midRow][mid] > target:
                right = mid - 1
            elif matrix[midRow][mid] < target:
                left = mid + 1
            else:
                return True
        return False