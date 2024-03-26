class Solution(object):
    def searchMatrix(self, matrix, target):
        # get the matrix dimension
        rows = len(matrix)
        cols = len(matrix[0])

        # find the midRow
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
            return False

        # find the midIndex
        left = 0
        right = cols - 1
        midRow = (top + bottom) // 2
        while left <= right:
            midIndex = (left + right) // 2
            if matrix[midRow][midIndex] > target:
                right = midIndex - 1
            elif matrix[midRow][midIndex] < target:
                left = midIndex + 1
            else:
                return True
        return False