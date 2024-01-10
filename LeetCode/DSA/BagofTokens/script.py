# Bag of Tokens -> Python3

'''
Explanation: First sort the tokens then set deque to deque of tokens. Set ans to bns to 0 and run a 
while loop deque exists and (power greater than or same as deque at 0 or bns) run another loop 
while loop deque exists and (power greater than or same as deque at 0). Inside inner loop decrement 
from power the deque popleft and increment bns by 1. In outer loop set ans to max of ans and bns 
and later check if deque and bns are true. Increment power by deque.pop and decrement bns by 1. 
Finally return 0.
'''

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (power >= deque[0] or bns):
            while deque and power >= deque[0]:
                power -= deque.popleft()
                bns += 1
            ans = max(ans, bns)
            if deque and bns:
                power += deque.pop()
                bns -= 1
        return ans