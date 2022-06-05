class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = (m*n)-1

        while(low <= high):
            middle = low + (high-low)//2
            if(matrix[middle//n][middle % n] > target):
                high = middle - 1
            if(matrix[middle//n][middle % n] < target):
                low = middle + 1
            if(matrix[middle//n][middle % n] == target):
                return True
        return False
