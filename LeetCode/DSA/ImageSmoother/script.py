# Image Smoother -> Python3

'''
Explanation: Set ans as deepcopy of img and a as len of img then b as len of first row in img if a 
is valid else 0. Then loop on a and b in nested for and set nbrs as array of all neighbours in img 
by looping on i and j if they are valid and set ans as the sum of nbrs floor div by len of nbrs 
then finally return ans.
'''

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans, a = deepcopy(img), len(img)
        b = len(img[0]) if a else 0
        for i in range(a):
            for j in range(b):
                nbrs = [img[_i][_j] for _i in (i - 1, i, i + 1) for _j in (j - 1, j, j + 1)
                        if 0 <= _i < a and 0 <= _j < b]
                ans[i][j] = sum(nbrs) // len(nbrs)
        return ans