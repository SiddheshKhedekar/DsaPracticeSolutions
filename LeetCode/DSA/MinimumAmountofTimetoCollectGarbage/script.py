# Minimum Amount of Time to Collect Garbage -> Python3

'''
Explanation: In dict lstIdx set each char to its last occurrence index in garbage then accumulate 
the distance from 0 of travel in dist. Finally return the sum of map len garbage added to the sum 
of the dist at lstidx at chr, 0 for chr in PGM.
'''

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        lstIdx = {chr: idx for idx, str in enumerate(garbage) for chr in str}
        dist = list(accumulate(travel, initial = 0))
        return sum(map(len, garbage)) + sum(dist[lstIdx.get(chr, 0)] for chr in 'PGM')