# UTF-8 Validation -> Python3

'''
Explanation: Set n_byetes to 0 and mask1 to 1 << 7 along with mask2 to 1<<6. Loop over data as num. 
Set mask 1<<7 and check if n_bytes == 0 true and run while loop inside until mask & num. Increment 
n_bytes by 1 and set mask to mast >> 1. Check if n_bytes == 0 and continueoutside while loop and 
also check if n_bytes == 1 or n_bytes > 4 adn return false. In else of outer if check if not (num & 
mask1 and not (num & mask2)) and return false if condition met outside conditions decrement n_bytes 
by 1. Return n_bytes == 0.
'''

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes+=1
                    mask = mask >> 1
                if n_bytes == 0: continue
                if n_bytes == 1 or n_bytes > 4: return False
            else:
                if not (num & mask1 and not (num & mask2)): return False
            n_bytes-=1
        return n_bytes == 0