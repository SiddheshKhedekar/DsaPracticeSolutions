# Capacity To Ship Packages Within D Days -> Python3

'''
Explanation: Set one pointer to max and other to sum. Run while loop till l is less than r and set 
mid need and current run for loop on weights and check when current plus weight is greater than mid 
and reset cur and increment need. Then update current with weight and out of for loop check need 
greater than days and set left to mid + 1 else set right to mid and finally return left.
'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m, need, current = (l + r) // 2, 1, 0
            for weight in weights:
                if current + weight > m:
                    need += 1
                    current = 0
                current += weight
            if need > days: l = m + 1
            else: r = m
        return l