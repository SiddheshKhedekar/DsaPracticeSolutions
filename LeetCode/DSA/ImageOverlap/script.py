# Image Overlap -> Python3

'''
Explanation: Two options either flatten by 100 and save the matrix in two arrays and then save the 
counter i-j in both array finally getting max c.values or [0]. Secondly by considering (i,j) of 
both matrix and same steps from counter just that here we have ax-bx, ay-by.
'''

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        LA = [i // N * 100 + i % N for i in range(N * N) if img1[i // N][i % N]]
        LB = [i // N * 100 + i % N for i in range(N * N) if img2[i // N][i % N]]
        c = Counter(i-j for i in LA for j in LB)
        return max(c.values() or [0])