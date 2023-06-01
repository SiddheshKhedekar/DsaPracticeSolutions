# Most Stones Removed with Same Row or Column -> Python3

'''
Explanation: Define uf as dict and run for loop on stones to set the uf at find i as the find ~j 
then return len stones minus the len of dict populated by find x for all x in uf. In find function 
check if x is not same as uf setdefault of x,x to set uf at x as find of uf at x and return uf at x.
'''

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x): uf[x] = find(uf[x])
            return uf[x]
        for i, j in stones: uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf})