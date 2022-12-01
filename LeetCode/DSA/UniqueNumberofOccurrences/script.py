# Unique Number of Occurrences -> Python3

'''
Explanation: Define a set and loop on the frequencies to check if already present in set.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = set()
        for f in collections.Counter(arr).values():
            if f in mem: return False
            mem.add(f)
        return True