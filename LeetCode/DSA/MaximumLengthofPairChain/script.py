# Maximum Length of Pair Chain -> Python3

'''
Explanation: Set crnt as max and ans as 0 then loop of sorted pairs where key is the item element 
at index 1. Check if crnt is less than pr at 0 to set crnt as pr at 1 and increment ans by 1.
'''

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        crnt, ans = float('-inf'), 0
        for pr in sorted(pairs, key=lambda i: i[1]):
            if crnt < pr[0]: crnt, ans = pr[1], ans + 1
        return ans