# Max Number of K-Sum Pairs -> Python3

'''
Explanation: Set count as counter of nums and res as 0 then loop on value in count and increment 
res by the min of count at value and count at k - value. Finally return res floor divided by 2.
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count, res = Counter(nums), 0
        for valu in count: res += min(count[valu], count[k - valu])
        return res // 2