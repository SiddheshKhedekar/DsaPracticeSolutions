# Eliminate Maximum Number of Monsters -> Python3

'''
Explanation: Loop on the enumerated idx, tim of the sorted array created by computing how many 
minutes each monster needs to reach the city, based on the initial position and speed. Then check 
if idx is greater than tim to return idx otherwise return len dist at end of function.
'''

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for idx, tim in enumerate(sorted([(dst - 1) // spd for dst, spd in zip(dist, speed)])):
            if idx > tim: return idx
        return len(dist)