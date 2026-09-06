class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Decompress the matrix into 1D
        size = len(matrix[0])* len(matrix)

        l = 0
        r = size - 1 

        while l <= r:
            mid = (l+r)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False


