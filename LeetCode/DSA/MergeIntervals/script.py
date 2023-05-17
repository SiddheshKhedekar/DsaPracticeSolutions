# Merge Intervals -> Python3

'''
Explanation: Initialize ans and then run loop on sorted intervals where key is the first from 
arrayitem then check if ans and first item of x is less than or same as the last item of the end of 
ans. Then set the last item of the end of ans as the max of itself ans last item of x else append x 
to ans.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for x in sorted(intervals, key=lambda x: x[0]):
            if ans and x[0] <= ans[-1][1]: ans[-1][1] = max(ans[-1][1], x[1])
            else: ans += x,
        return ans