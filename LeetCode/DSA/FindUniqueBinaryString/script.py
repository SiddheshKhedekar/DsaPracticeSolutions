# Find Unique Binary String -> Python3

'''
Explanation: Define empty string as res then run loop on enumerated x, n in nums. Then we check if 
n at x is 0 to add 1 to string res else 0 which is the implementation of Cantor's Diagonalization 
technique and at end of loop return res.
'''

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        for x, n in enumerate(nums): res += '1' if n[x] == '0' else '0'
        return res