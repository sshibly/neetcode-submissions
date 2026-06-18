class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get dimensions of the matrix (number of rows, cols)
        rows = len(matrix)
        cols = len(matrix[0])

        # look for the row we need to find
        # top row pointer and bottom row pointer
        top = 0 
        bot = rows - 1

        # find the target row, or it might not exist in the binary search
        while top <= bot: 
            mid_row = (top + bot) // 2
            
            # look at the rightmost value
            # check if the target value is greater
            # than the largest value in this row
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False

        # time complexity: O(m + n)
        # space complexity: O(1)







