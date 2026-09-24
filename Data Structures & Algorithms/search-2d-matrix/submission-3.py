class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        # first column search
        T, B = 0, R - 1
        while T <= B:
            row = (T + B) // 2
            if target > matrix[row][-1]:
                T = row + 1
            elif target < matrix[row][0]:
                B = row - 1
            else:
                break
        # then do the friggin row search 
        row  = (T + B) // 2
        left, right = 0, C - 1
        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif target > matrix[row][col]:
                left = col + 1
            else:
                return True
        return False