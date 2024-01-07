# Minimum Number of Operations to Make Array Empty -> Python3

'''
Explanation: If the one value frequency is 1, then it can't be removed. So we save the freq in cnt 
and return -1 if 1 in cnt otherwise the sum of (x + 2) floor divide by 3 for all x in cnt.
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums).values()
        return - 1 if 1 in cnt else sum((x + 2) // 3 for x in cnt)