# Delete and Earn -> Python3

'''
Explanation: Set frequencies and prev, cur to 0 then loop on max range and set prev, cur to cur, 
max of prev+iterator*(freq of iterator), cur.
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, cur = Counter(nums), 0, 0
        for value in range(10001):
            prev, cur = cur, max(prev+value*points[value], cur)
        return cur