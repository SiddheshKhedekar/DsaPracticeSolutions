# Combinations -> Python3

'''
Explanation: Initialise sol to [] and call backtrack passing k, [] and 1, below that return sol. In 
backtrack check if remainder is 0 and do sol.append(co.copy) else run for loop from nex to n+1. 
Inside append i to co and call backtrack with remain-1, comb and i+1 and pop co.
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtrack(remain, comb, nex):
            if remain == 0: sol.append(comb.copy())
            else:
                for i in range(nex, n+1):
                    comb.append(i)
                    backtrack(remain-1,comb,i+1)
                    comb.pop()
        backtrack(k,[],1)
        return sol