# Add Digits -> Python3

'''
Explanation: We know 0 has digital root 0 and for any number divisible by 9 it has digital root 9. 
Knowing that we can also have digital root for all remaining digits from 1 to 8 as num % 9.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if num % 9 == 0: return 9
        else: return num % 9