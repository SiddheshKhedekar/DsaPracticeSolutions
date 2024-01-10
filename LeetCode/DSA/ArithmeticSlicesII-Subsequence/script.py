# Arithmetic Slices II - Subsequence -> Python3

'''
Explanation: Set n as len of nums then res as 0 and mem as array of defaultdict as int in the range 
n. Then run a loop on range 1 ot n and nest loop for range i then set diff as the difference 
between nums at i and j. Set count as 0 and check if diff in mem at j to set the count as mem at j, 
diff then increment mem at i, diff by count + 1 and res by count. Finally return res at end.
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        mem = [defaultdict(int) for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = 0
                if diff in mem[j]: count = mem[j][diff]
                mem[i][diff] += count + 1
                res += count
        return res