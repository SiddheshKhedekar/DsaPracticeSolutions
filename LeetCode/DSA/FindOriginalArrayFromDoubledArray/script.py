# Find Original Array From Doubled Array -> Python3

'''
Explanation: Using collections.Counter save the frequencies on arr. If frequency of 0 in c % 2 is 
1 return []. Using for iterate over sorted c with x. If c[x] > c[2*x] return []. Decrement 
frequency of c[2*x] by c[x] if x else floor divide c[x] by 2. Return list of c.elements.
'''

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0] % 2: return []
        for x in sorted(c):
            if c[x] > c[2*x]: return []
            c[2*x] -= c[x] if x else c[x]//2
        return list(c.elements())