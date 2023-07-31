# Maximum Running Time of N Computers -> Python3

'''
Explanation: Sort the batteries and save summ as the sum of batteries then run loop while batteries 
at last index is greater than summ divided by n. Inside decrement n by 1 and summ by batteries pop 
at end return the floor division of summ by n.
'''

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        summ = sum(batteries)
        while batteries[-1] > summ / n:
            n -= 1
            summ -= batteries.pop()
        return summ // n