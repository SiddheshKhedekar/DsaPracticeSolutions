# Restore the Array From Adjacent Pairs -> Python3

'''
Explanation: Build a graph to locate the ends and access its pairs, then traverse the graph and 
find one end. From end we loop to find the next element, we know that for each key in graph there 
are at most 2 neighbors of which one has already been found and other is next element, we continue 
this till len condition satisfied.
'''

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nb, res, l = defaultdict(list), [], len(adjacentPairs) + 1
        for x, y in adjacentPairs:
            nb[x] += [y]
            nb[y] += [x]
        pre = -math.inf
        for x, y in nb.items():
            if len(y) == 1:
                res += [x]
                break
        while len(res) < l:
            for nxt in nb.pop(res[-1]):
                if nxt != pre:
                    pre = res[-1]
                    res += [nxt]
                    break
        return res