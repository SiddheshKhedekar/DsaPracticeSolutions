# Most Stones Removed with Same Row or Column -> Python3

'''
Explanation: We can remove a stone if and only if, there is another stone in the same column or 
row. We try to remove as many as stones as possible. Connected stones will build a connected graph. 
In one connected graph, we can't remove all stones we need one stone left. The elements are not the 
points, but the indexes. For each point, union two indexes then return points number - union 
number. For implementing union find we use dict uf and define find function. Loop on stones in main 
function to set the uf at find i ans find ~j then return the len of stones - the len of find x for 
x in uf. Inside find we check if x and uf setdefault is not same to set uf at x as find of uf at x 
and return uf at x.
'''

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x): uf[x] = find(uf[x])
            return uf[x]
        for i, j in stones: uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf})