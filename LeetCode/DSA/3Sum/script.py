# 3Sum -> Python3

'''
Explanation: Split nums into lists of negatives, positives, and zeros. Create a separate set for 
negatives and positives. If there is at least 1 zero in the list, add all cases where -num exists 
in N and num exists in P. If there are at least 3 zeros in the list then also include that. For all 
pairs of negative numbers, check to see if their complement exists in the positive number set and 
vice versa.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n, p, z, = set(), [], [], []
        for num in nums:
            if num > 0: p.append(num)
            elif num < 0: n.append(num)
            else: z.append(num)
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N: res.add((-1*num, 0, num))
        if len(z) >= 3: res.add((0, 0, 0))
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P: res.add(tuple(sorted([n[i], n[j], target])))
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N: res.add(tuple(sorted([p[i], p[j], target])))
        return res