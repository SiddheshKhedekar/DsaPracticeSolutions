# Solving Questions With Brainpower -> Python3

'''
Explanation: Write a cached recursive dfs function with x as input and in main function return dfs 
call to 0. Inside dfs we return 0 if len questions is less than x else return max of recursive call 
to dfs x + 1 or points of x + recursive call to dfs with x + 1 + brainpower at x.
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(x):
            return 0 if x >= len(questions) else \
                max(dfs(x + 1), questions[x][0] + dfs(x + 1 + questions[x][1]))
        return dfs(0)