# Min Cost Climbing Stairs -> Python3

'''
Explanation: Loop over array in reverse order from third last value and increment the ith value by 
min of its next two elements. Finally return the min of the first two values in array.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])