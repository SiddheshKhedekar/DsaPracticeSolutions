# Jump Game III -> Python3

'''
Explanation: Check if start is in constraint and arr at start is greater than or smae as 0 then 
inside set arr at start as its negative and return if arr at start is 0 or the recursive call of 
arr and start + arr at start or the recursive call of arr and start - arr at start. Otherwise at 
end return False.
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or \
                self.canReach(arr, start - arr[start])
        return False