# Reveal Cards In Increasing Order -> Python3

'''
Explanation: Initialize empty deque as dq then loop on reverse sorted deck using i. Inside rotate 
dq and append i in it from left then on loop end return list of dq.
'''

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq = deque()
        for i in sorted(deck)[::-1]:
            dq.rotate()
            dq.appendleft(i)
        return list(dq)