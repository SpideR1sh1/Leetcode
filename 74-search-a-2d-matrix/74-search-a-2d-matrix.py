class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m, n = len(matrix[0]), len(matrix)
        r = m * n - 1
        
        while l < r:
            med = (l + r) // 2
            
            if matrix[med//m][med%m] < target:
                l = med + 1
            else:
                r = med
        return matrix[l//m][l%m] == target

        