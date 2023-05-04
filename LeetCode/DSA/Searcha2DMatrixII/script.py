# Search a 2D Matrix II -> Python3

'''
Explanation: Set x, y as the len of matrix, len of matrix and len of its first row. Also set row as 
0 and col as y-1 and run a while loop till row is less than x and col is greater than or same as 0. 
Start from rightmost point in matrix and check if target is greater than matrix at row and col then 
increment row by 1 and move to next row. Else if target is less than matrix at row col then 
decrement col by 1 and move to next column. Else return true and on loop end return false.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix), len(matrix) and len(matrix[0])
        row, col = 0, y - 1
        while row < x and col >= 0:
            if target > matrix[row][col]: row += 1
            elif target < matrix[row][col]: col -= 1
            else: return True
        return False