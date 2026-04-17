class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = (m * n) - 1
        
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n #mid - (n * i)
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                return True
        return False

