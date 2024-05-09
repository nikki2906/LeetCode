class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if matrix[midRow][0] > target:
                bottom = midRow - 1    
            elif matrix[midRow][-1] < target:
                top = midRow + 1
            else:
                break
        
        if not(top <= bottom):
            return 

        left = 0 
        right = cols - 1
        midRow = (top + bottom) // 2
        while left <= right:
            midPoint = (left + right) // 2
            if matrix[midRow][midPoint] > target:
                right = midPoint - 1
            elif matrix[midRow][midPoint] < target:
                left = midPoint + 1
            else:
                return True
        return False
            