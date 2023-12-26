# Parallel Courses III -> Python3

'''
Explanation: Set grph as defaultdict of list then loop on relations using i, j to increment grph at 
j by arrayitem i. Outside loop set dp as the cache of lambda function i as time at i - 1 + max of 
dp at j for each in grph at i after 0 added to the array. Finally return the max of dp at k + 1 for 
each k in range n.
'''

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        grph = defaultdict(list)
        for i, j in relations: grph[j] += [i]
        dp = cache(lambda i:time[i - 1] + max([dp(j) for j in grph[i]] + [0]))
        return max(dp(k + 1) for k in range(n))