# Letter Case Permutation -> Python3

'''
Explanation: Initialize empty array and use list comprehension along with loops to populate array 
with use of swapcase function on each character in string.
'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for c in s:
            ans = [x + cc for x in ans for cc in {c,c.swapcase()}]
        return ans