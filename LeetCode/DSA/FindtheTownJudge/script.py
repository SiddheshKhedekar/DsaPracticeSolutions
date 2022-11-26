# Find the Town Judge -> Python3

'''
Explanation: Get the count of all trusted people in an array and then for all people check if any 
single person trust count is number of people-1. 
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n+1)
        for i, j in trust:
            count[i]-=1
            count[j]+=1
        for i in range(1,n+1):
            if count[i] == n-1:
                return i
        return -1