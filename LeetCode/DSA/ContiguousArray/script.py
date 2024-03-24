# Contiguous Array -> Python3

'''
Explanation: Set cnt, mlen to 0 and tab as dict with 0 key value then loop for i, val in nums, 1 
and check if val is 0 to decrement cnt by 1 else increment by 1. Then check if cnt in tab to set 
mlen to max of itself and i - tab at cnt else set tab at cnt as i then at end return mlen.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, mLen, tab = 0, 0, {0: 0}
        for i, val in enumerate(nums, 1):
            if val == 0: cnt -= 1
            else: cnt += 1
            if cnt in tab: mLen = max(mLen, i - tab[cnt])
            else: tab[cnt] = i
        return mLen