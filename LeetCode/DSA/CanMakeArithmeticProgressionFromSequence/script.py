# Can Make Arithmetic Progression From Sequence -> Python3

'''
Explanation: Sort arr and set prog as arr at 1 - arr at 0. Then run loop for i in the range from 1 
to len arr -1 and inside check if arr at i+1 - arr at i is not same as prog and return false. At 
end return True.
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        prog = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i] != prog: return False
        return True