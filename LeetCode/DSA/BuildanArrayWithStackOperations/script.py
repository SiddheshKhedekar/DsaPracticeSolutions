# Build an Array With Stack Operations -> Python3

'''
Explanation: Set ans as empty array and stk as set of target then run loop on range 1 to last item 
in target + 1. Inside loop insert push in ans then check if x not in stk to pop. At end return ans.
'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans, stk = [], set(target)
        for x in range(1, target[-1] + 1):
            ans.append('Push')
            if x not in stk: ans.append('Pop')
        return ans 