# Gas Station -> Python3

'''
Explanation: Given that journey between stations is curcular we need to run a loop on number of 
stations. Then set total surplus and surplus by incrementing them by difference between gas and 
cost at current index. If surplus becomes 0 then we set start to next index and finally return -1 
if total surplus is less than 0 else start.
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start