import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case check: empty matrix
        if not matrix:
            return False

        # Find the size
        row = len(matrix)
        col = len(matrix[0])

        # Initialize
        left = 0
        right = row * col - 1

        # Binary search
        while left <= right:
            mid = (left + right)//2
            # Determine index
            r_i = math.floor(mid/col)
            c_i = mid % col

            if matrix[r_i][c_i] < target:
                left = mid + 1
            elif matrix[r_i][c_i] > target:
                right = mid - 1
            else:
                return True
        
        return False


        