# Add to Array-Form of Integer -> Python3

'''
Explanation: Add the element to last element of array and rin for loop in reverse on num elements. 
Set carry and num at i to divmod num at i, 10. If i then increment num at i-1 by carry. Out of loop 
if carry set num to list map int cast str(carry) + num and return num.
'''

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        for i in range(len(num)-1,-1,-1):
            carry, num[i] = divmod(num[i], 10)
            if i: num[i-1] += carry
        if carry: num = list(map(int,str(carry))) + num
        return num