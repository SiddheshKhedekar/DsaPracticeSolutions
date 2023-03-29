# Minimum Cost For Tickets -> Python3

'''
Explanation: Set mem as array of 0 the size of 1 greater than last item in days. Run a for loop on 
the same range as before and if x not in days then set mem at x as the one at its previous index. 
Else set mem at x as the min of the mem max index of 0 and x-i plus cost at j. Where i is the day 
pass and j is the respective cost.
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mem = [0 for _ in range(days[-1] + 1)]
        for x in range (days[-1] + 1):
            if x not in days: mem[x] = mem[x - 1]
            else: 
                mem[x] = min(mem[max(0, x - 1)] + costs[0], mem[max(0, x - 7)] + costs[1], 
                    mem[max(0, x - 30)] + costs[2])
        return mem[-1]