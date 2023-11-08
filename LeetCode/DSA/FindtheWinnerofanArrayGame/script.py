# Find the Winner of an Array Game -> Python3

'''
Explanation: Set crnt as arr at 0 and wcnt as 0 then run loop on range len arr. Inside loop check 
if arr at x is greater than crnt to set crnt as arr at x and also set wcnt to 0 then increment wcnt 
by 1 and check if wcnt is k to break. Finally return crnt.
'''

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        crnt, wCnt = arr[0], 0
        for x in range(1, len(arr)):
            if arr[x] > crnt: crnt, wCnt = arr[x], 0
            wCnt += 1
            if wCnt == k: break
        return crnt