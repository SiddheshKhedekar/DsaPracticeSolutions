# Bulb Switcher -> Python3

'''
Explanation: Bulbs in range n are switched on or off in n rounds where for ith round the i bulbs 
are skipped before toggle. Divisors come in pairs except when i is a square so bulb i ends up on 
if i is a square. We can get the answer with integer sqrt for non perfect square numbers and also 
verify results with dry run.
'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return isqrt(n)