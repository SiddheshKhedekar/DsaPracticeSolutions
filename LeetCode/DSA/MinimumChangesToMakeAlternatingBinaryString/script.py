# Minimum Changes To Make Alternating Binary String -> Python3

'''
Explanation: We can observe that the sequence of index mod by 2 is the sequence we want so we save 
the sum as ans after checking if it is same as the char in loop of s then return the minor ans and 
the len of s - ans.
'''

class Solution:
    def minOperations(self, s: str) -> int:
        ans = sum(x % 2 == int(char) for x, char in enumerate(s))
        return min(ans, len(s) - ans)