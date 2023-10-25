# Flood Fill -> Python3

'''
Explanation: Set rc, cc and col to len image, len image[0] and image [sr][sc]. Check if col is 
colour passed and return image. Write a dfs function where sr and sc are passed check if image r c 
= col and inside set image r c to color. Check if r >= 1 then dfs(r-1,c). Similarly if r+1 < rc 
then dfsp(r+1, c), if c >= 1 then dfsp(r, c-1) and if c+1 < cc then dfsp(r, c+1). Run dfs and 
return image.
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rc, cc = len(image), len(image[0])
        col  = image[sr][sc]
        if col == color: return image
        def dfsp(r, c):
            if image[r][c] == col:
                image[r][c] = color
                if r >= 1: dfsp(r-1, c)
                if r+1 < rc: dfsp(r+1, c)
                if c >= 1: dfsp(r, c-1)
                if c+1 < cc: dfsp(r, c+1)
        dfsp(sr, sc)
        return image