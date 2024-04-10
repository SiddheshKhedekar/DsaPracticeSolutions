# Time Needed to Buy Tickets -> Python3

'''
Explanation: Loop on enumerated tickets using x, y and return the sum of the min of y, tickets at k 
if x is less than or same as k otherwise tickets at k value - 1.
'''

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(y, tickets[k] if x <= k else tickets[k] - 1) for x, y in enumerate(tickets))