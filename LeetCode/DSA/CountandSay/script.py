# Count and Say -> Python3

'''
Explanation: Set start value s to string 1 then run for loop in range n-1 and inside set s to a 
string using join a combination of group and digit which we can get after groupby on s.
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1): 
            s = ''.join(str(len(list(group))) + digit 
            for digit, group in itertools.groupby(s))
        return s