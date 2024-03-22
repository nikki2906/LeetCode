class Solution(object):
    def searchMatrix(self, matrix, target):
        # get the dimension of the matrix
        rows = len(matrix) 
        cols = len(matrix[0])

        # find the middle row
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if matrix[midRow][0] > target:
                bottom = midRow - 1
            elif matrix[midRow][-1] < target:
                top = midRow + 1
            else:
                break
        if not(top <= bottom):
            return False
        
        midRow = (top + bottom) // 2
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            midCol = (left + right) // 2
            if matrix[midRow][midCol] > target:
                right = midCol - 1
            elif matrix[midRow][midCol] < target:
                left = midCol + 1
            else:
                return True
        return False
