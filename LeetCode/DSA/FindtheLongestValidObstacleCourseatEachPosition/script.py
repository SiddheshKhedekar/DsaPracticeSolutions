# Find the Longest Valid Obstacle Course at Each Position -> Python3

'''
Explanation: Set incarr and ans as empty array then loop on x in obstacles. Inside set y as bisect 
of incarr, x then append y + 1 to ans. Check if y is same as len incarr to append 0 to incarr and 
set incarr at y to x.
'''

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        incArr, ans = [], []
        for x in obstacles:
            y = bisect.bisect(incArr, x)
            ans.append(y + 1)
            if y == len(incArr): incArr.append(0)
            incArr[y] = x
        return ans