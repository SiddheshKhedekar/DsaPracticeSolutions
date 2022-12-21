# Daily Temperatures -> Python3

'''
Explanation: Enumerate on temperatures and inside while loop when temperature at last stack 
position is less than current temp then set current index by popping stack and set ans at current 
index the diff between index in for loop - current index. Append i to stack after while loop.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [0]*len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans