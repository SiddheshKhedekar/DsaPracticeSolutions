# House Robber -> Python3

'''
Explanation: Use two variables set to 0 and iterate on nums array. every iteration set last to now 
and in now set the max of last+(current value of array iteration) and now.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums: last , now = now, max(last+i, now)
        return now