# Best Team With No Conflicts -> Python3

'''
Explanation: Sort the inputs first and define memory for max size. Then run for loop on length and 
set memory for iterator. Run another loop of iterator and check for condition and update memory by
max. Finally return the max in memory.
'''

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sortedInputs = sorted(zip(ages, scores))
        l = len(sortedInputs)
        mem = [0] * l
        for x in range(l):
            mem[x] = sortedInputs[x][1]
            for y in range(x):
                if sortedInputs[y][1] <= sortedInputs[x][1]:
                    mem[x] = max(mem[x], mem[y] + sortedInputs[x][1])
        return max(mem)