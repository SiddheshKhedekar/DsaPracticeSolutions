# The Number of Weak Characters in the Game -> Python3

'''
Explanation: Sort array considering key such that the first item subset is negative. Then run loop 
and increment count if defence is less than current max else set current max to defence.
'''

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        ans, cur_max = 0, 0
        for _, d in properties: 
            if d < cur_max: ans+=1
            else: cur_max = d
        return ans