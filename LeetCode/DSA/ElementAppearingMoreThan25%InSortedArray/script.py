# Element Appearing More Than 25% In Sorted Array -> Python3

'''
Explanation: Set cnt as defaultdict of int then set goal as the len of arr divided by 4. Then loop 
for each no in arr and increment cnt of no by one check if cnt no is greater than goal and return 
no otherwise return -1 at end.
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt, goal = defaultdict(int), len(arr) / 4
        for no in arr:
            cnt[no] += 1
            if cnt[no] > goal: return no
        return -1