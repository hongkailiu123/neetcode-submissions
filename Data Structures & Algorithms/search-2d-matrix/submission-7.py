class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        colLength = len(matrix[0])
        leftIndex = 0
        rightIndex = len(matrix) * len(matrix[0]) - 1

        while leftIndex <= rightIndex:
            mid = (rightIndex + leftIndex) // 2
            r = mid // colLength
            c = mid - colLength * r 

            if target == matrix[r][c]:
                return True
            if target < matrix[r][c]:
                rightIndex = mid - 1
            if target > matrix[r][c]:
                leftIndex = mid + 1
              
        
        return False
        