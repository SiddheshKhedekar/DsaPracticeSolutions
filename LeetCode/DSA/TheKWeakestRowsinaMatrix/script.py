# The K Weakest Rows in a Matrix -> Python3

'''
Explanation: We sort the matrix on index and save the order in a array and return the k smallest.
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = len(mat)
        out = sorted(range(l), key=lambda i: (mat[i], i))
        del out[k:]
        return out