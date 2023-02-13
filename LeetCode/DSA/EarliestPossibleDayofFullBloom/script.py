# Earliest Possible Day of Full Bloom -> Python3

'''
Explanation: Planting non-consecutively does not alter the optimum outcome obtained from the 
alternative. It is needed to sort the plants by descending growth time and find the time it takes 
for them to bloom and update the result till the final one.
'''

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        temp_planttime, res = 0, 0
        indxs = sorted(range(len(plantTime)), key = lambda x: -growTime[x])
        for i in indxs:
            temp_planttime += plantTime[i]
            res = max(res, temp_planttime + growTime[i])
        return res